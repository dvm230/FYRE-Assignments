import machine # module with all microcontroller stuff
import time # module with sleep

led = machine.Pin(0,machine.Pin.OUT) # Green LED object

while(True): # infinite loop
  led.value(1) # Turn on green LED
  time.sleep(0.25) # quarter second delay
  led.value(0) # Turn off green LED
  time.sleep(0.25)