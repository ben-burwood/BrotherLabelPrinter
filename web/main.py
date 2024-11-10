import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import BrotherPrinterApiError
from .config import Config
from .printer_manager import PrinterManager
from .routes.config import router as config_router
from .routes.print import router as print_router

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = Config.get()
    if config.backend is None or config.printer is None:
        raise BrotherPrinterApiError("Must Provide a Valid Backend AND Printer Configuration")

    PrinterManager.toggle_power_button(config.motor_initial, config.motor_pressed)
    time.sleep(5)

    PrinterManager(config.backend, config.printer, config.vendor_id, config.product_id)

    yield


app.router.lifespan_context = lifespan
app.include_router(config_router)
app.include_router(print_router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/health")
def health():
    return {"status": "ok"}
