import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from labelprinterkit.job import Job

from api import BrotherPrinterApiError
from api.config import Config
from api.print_request import PrintRequest
from api.printer_manager import PrinterManager

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = Config()
    if config.backend is None or config.printer is None:
        raise BrotherPrinterApiError("Must Provide a Valid Backend AND Printer Configuration")

    global printer_manager
    printer_manager = PrinterManager(config.backend, config.printer)

    printer_manager.toggle_power_button()
    time.sleep(5)

    yield


app.router.lifespan_context = lifespan


@app.get("/print")
def print_label(request: PrintRequest):
    printer = printer_manager.printer

    label = request.generate_label(request.media)

    job = Job(request.media)
    job.add_page(label)

    printer.print(job)

    return {"status": "success", "message": "Label printed successfully"}
