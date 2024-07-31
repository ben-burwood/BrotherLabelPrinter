from enum import Enum

from labelprinterkit.backends.bluetooth import BTSerialBackend
from labelprinterkit.backends.network import NetworkBackend
from labelprinterkit.backends.usb import PyUSBBackend
from labelprinterkit.printers import BackendType

class ConnectionType(Enum):
    USB = "USB"
    WIFI = "WiFi"
    BLUETOOTH = "Bluetooth"

    @property
    def backend(self) -> BackendType:
        match self:
            case ConnectionType.USB:
                return PyUSBBackend()
            case ConnectionType.BLUETOOTH:
                return BTSerialBackend("")
            case ConnectionType.WIFI:
                return NetworkBackend("")

    @staticmethod
    def get_by_value(name: str) -> "ConnectionType":
        for connection_type in ConnectionType:
            if connection_type.value == name:
                return connection_type
        raise ValueError(f"ConnectionType with name {name} not found")
