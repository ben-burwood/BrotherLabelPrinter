from enum import Enum


class ConnectionType(Enum):
    USB = "USB"
    WIFI = "WiFi"
    BLUETOOTH = "Bluetooth"

    @staticmethod
    def get_by_name(name: str) -> "ConnectionType":
        for connection_type in ConnectionType:
            if connection_type.value == name:
                return connection_type
        raise ValueError(f"ConnectionType with name {name} not found")
