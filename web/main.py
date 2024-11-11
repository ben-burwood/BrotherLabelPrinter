import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .printer_manager import PrinterManager
from .routes.print import router as print_router
from .settings import Settings

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()

    PrinterManager.toggle_power_button(settings.motor_initial, settings.motor_final)
    time.sleep(5)

    PrinterManager(
        settings.backend, settings.printer, settings.vendor_id, settings.product_id
    )

    yield


app.router.lifespan_context = lifespan
app.include_router(print_router)


@app.get("/health")
def health():
    return {"status": "ok"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
