import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from labelprinterkit.job import Job

from . import BrotherPrinterApiError
from .config import Config
from .print_request import PrintRequest
from .printer_manager import PrinterManager

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = Config()
    if config.backend is None or config.printer is None:
        raise BrotherPrinterApiError("Must Provide a Valid Backend AND Printer Configuration")


    PrinterManager.toggle_power_button(config.motor_initial, config.motor_pressed)
    time.sleep(10)

    global printer_manager
    printer_manager = PrinterManager(config.backend, config.printer)

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
