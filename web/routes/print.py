from brother_label_printer_control.job import Job
from fastapi import APIRouter, Depends

from ..print_request import PrintRequest
from ..printer_manager import PrinterManager
from ..settings import Settings

router = APIRouter()


def get_printer_manager(config: Settings = Depends(Settings)) -> "PrinterManager":
    return PrinterManager(config.backend, config.printer)


@router.get("/print")
@router.post("/print")
def print_label(
    request: PrintRequest,
    printer_manager: PrinterManager = Depends(get_printer_manager),
):
    printer = printer_manager.printer

    label = request.generate_label(request.media)

    job = Job(request.media)
    job.add_page(label)

    printer.print(job)

    return {"status": "success", "message": "Label printed successfully"}
