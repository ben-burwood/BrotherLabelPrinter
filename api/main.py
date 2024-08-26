from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel

from api.PrinterManager import PrinterManager
from api.config import get_font
from labelprinterkit.constants import Media
from labelprinterkit.job import Job
from labelprinterkit.labels.box import Box
from labelprinterkit.labels.label import Label
from labelprinterkit.labels.text import Padding, Text
from labelprinterkit.printers.main import Printer
from labelprinterkit.utils.font import get_fonts

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global printer_manager
    printer_manager = PrinterManager(Printer.PTP_700)
    yield


app.router.lifespan_context = lifespan


class PrintRequest(BaseModel):
    text: str
    height: int
    font: str = get_font()

    @property
    def label(self) -> Label:
        text = Text(self.height, self.text, list(get_fonts().values())[0][0].as_posix(), padding=Padding(0, 10, 0, 0))
        box = Box(70, text)
        return Label(box)


@app.get("/print")
def print_label(request: PrintRequest):
    printer = printer_manager.printer

    label = request.label

    job = Job(Media.W12)
    job.add_page(label)

    printer.print(job)

    return {"status": "success", "message": "Label printed successfully"}
