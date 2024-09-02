import subprocess

from motor.constants import PWM_PATH, PWM_PERIOD, MotorPosition


class Motor:

    def __init__(self, pwm_channel: int = 1) -> None:
        self.pwm_channel = pwm_channel
        self.pwm_channel_path = f"{PWM_PATH}/pwm{pwm_channel}"

        self._setup_pwm()
        self._set_period(PWM_PERIOD)

    @staticmethod
    def _setup_pwm() -> None:
        try:
            subprocess.run(f"echo 1 > {PWM_PATH}/export", shell=True, check=True)
        except subprocess.CalledProcessError:
            # If the PWM Channel is already exported, pass
            pass

    def _set_period(self, period: int) -> None:
        """The Period is the time it takes to complete one cycle"""
        subprocess.run(f"echo {period} > {self.pwm_channel_path}/period", shell=True, check=True)

    def _set_duty_cycle(self, duty_cycle: int) -> None:
        """The Duty Cycle is the percentage of cycle that the signal is High"""
        subprocess.run(f"echo {duty_cycle} > {self.pwm_channel_path}/duty_cycle", shell=True, check=True)

    def _set_enabled(self, enabled: bool) -> None:
        """Enable or Disable the Motor"""
        state = 1 if enabled else 0
        subprocess.run(f"echo {state} > {self.pwm_channel_path}/enable", shell=True, check=True)

    def enable_pwm(self) -> None:
        self._set_enabled(True)

    def disable_pwm(self) -> None:
        self._set_enabled(False)

    def set_position(self, position: MotorPosition) -> None:
        """Set the Motor Position"""
        self._set_duty_cycle(position.value)

    def set_position_percentage(self, percentage: int) -> None:
        """Set the Motor Position by Percentage of the Position Between Full Left to Full Right"""
        position_value = MotorPosition.percentage(percentage)
        self._set_duty_cycle(position_value)
