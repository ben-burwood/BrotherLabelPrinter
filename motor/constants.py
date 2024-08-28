from enum import Enum


PWM_PATH = "/sys/class/pwm/pwmchip0"


PWM_PERIOD = 20000000  # 20ms = 50 Hz


class MotorPosition(Enum):
    LEFT = 1000000  # 1ms Pulse
    CENTER = 1500000  # 1.5ms Pulse
    RIGHT = 2000000  # 2ms Pulse
