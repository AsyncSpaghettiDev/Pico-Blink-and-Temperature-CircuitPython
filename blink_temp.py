# CircuitPython Blink Example

import time
import board
import digitalio

import microcontroller

led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT


while True:
  print("Turned On!")
  led.value = True
  print(microcontroller.cpu.temperature)
  time.sleep(0.5)
  
  print("Turned Off!")
  led.value = False
  time.sleep(0.5)
