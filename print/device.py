from enum import Enum, auto

from labelprinterkit.printers import BackendType, E500, E550W, GenericPrinter, H500, P700, P750W


class Device(Enum):
    PTP_700 = auto()
    PTP_750W = auto()
    PTP_H500 = auto()
    PTP_E500 = auto()
    PTP_E550W = auto()

    def printer(self, backend: BackendType) -> GenericPrinter:
        match self:
            case Device.PTP_700:
                return P700(backend)
            case Device.PTP_750W:
                return P750W(backend)
            case Device.PTP_H500:
                return H500(backend)
            case Device.PTP_E500:
                return E500(backend)
            case Device.PTP_E550W:
                return E550W(backend)
