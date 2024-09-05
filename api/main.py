import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from labelprinterkit.job import Job

from . import BrotherPrinterApiError
from .config import Config, read_config, write_config
from .print_request import PrintRequest
from .printer_manager import PrinterManager

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = Config.get()
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



@app.get("/config")
def get_config():
    return Config.get().to_dict()


@app.post("/config/{config_item}")
def update_config(config_item: str, value: str):
    config = read_config()
    if config_item not in config:
        raise HTTPException(status_code=404, detail="Config item not found")

    config[config_item] = value
    write_config(config)

    return {"message": f"{config_item} updated to {value} successfully"}
