from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.PrinterManager import PrinterManager
from api.print import PrintRequest
from labelprinterkit.constants import Media
from labelprinterkit.job import Job
from labelprinterkit.printers.main import Printer

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global printer_manager
    printer_manager = PrinterManager(Printer.PTP_700)
    yield


app.router.lifespan_context = lifespan


@app.get("/print")
def print_label(request: PrintRequest):
    printer = printer_manager.printer

    label = request.label

    job = Job(Media.W12)
    job.add_page(label)

    printer.print(job)

    return {"status": "success", "message": "Label printed successfully"}
