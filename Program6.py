#Team member names: Annalise Dubeck, Daniel Mai, Emma Carothers
#Purpose of the code: Moves a servo 180 degrees when a button is pressed.
#Date code was started: 9/16/2026
#Date of last update: 9/16/2026
#Explanation of AI use: Helped set up circuit and coded the majority of the program

from machine import Pin, PWM
import time

# Pins
SWITCH_PIN = 18    # D9 on Nano ESP32
SERVO_PIN = 9      # D6 on Nano ESP32

# Button connected between D9 and GND
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)

# SG90 servo: 50 Hz PWM
servo = PWM(Pin(SERVO_PIN), freq=50)


def servo_angle(angle):
    """Move SG90 to 0-180 degrees."""

    angle = max(0, min(180, angle))

    # 1000 us = approximately 0 degrees
    # 2000 us = approximately 180 degrees
    pulse_us = 1000 + (angle * 1000 // 180)

    duty = int(pulse_us * 65535 / 20000)

    servo.duty_u16(duty)


# --------------------------------
# Initial setup
# --------------------------------

angle = 0
servo_angle(angle)

# Initial button state
previous = switch.value()


# --------------------------------
# Main loop
# --------------------------------

while True:

    # Read button
    current = switch.value()

    # --------------------------------
    # Detect a new button press
    # --------------------------------

    if previous == 1 and current == 0:

        # Small debounce delay
        time.sleep_ms(50)

        # Read again after debounce
        if switch.value() == 0:

            # Toggle servo
            if angle == 0:
                angle = 180
            else:
                angle = 0

            servo_angle(angle)

    # Remember current button state
    previous = current


    # --------------------------------
    # Debug output
    # --------------------------------

    if current == 0:
        button_state = "PRESSED"
    else:
        button_state = "NOT PRESSED"

    print("Servo angle:", angle,
          "degrees | Button:", button_state)

    # Controls how often debug information is printed
    time.sleep_ms(100)
