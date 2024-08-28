# Servo Motor Control

The OrangePi Zero3 has a built-in PWM controller that can be used to control servo motors.

http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_3#26pin_interface_GPIO.2C_I2C.2C_UART.2C_SPI_and_PWM_test

Allow PWM on Linux: http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_3#PWM_test_method:~:text=3%3A%20%2D%3E%203%5EC-,PWM,-test%20method

## Pins

The PWM pins are on the 26-pin GPIO header.

This Script uses PWM1 on Pin 10, this requires ph-pwm12 to be enabled.

## Servo Motor

The SG90 Servo Motor has a 180 deg Operating Range.

http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf

Positions:

- 1 ms Pulse: Left Extent
- 1.5 ms Pulse: Middle
- 2 ms Pulse: Right Extent
