"""
Let's all LEDs of the circuit blink in rainbow colors with a small time delay
"""

# import CPX library
from adafruit_circuitplayground.express import cpx
import time
from random import seed
from random import randint

seed(1)
cpx.pixels.brightness = 0.3

while True:
  i = 0

  while i < 10:
    newcolor = (randint(0, 255), randint(0, 255), randint(0,255))
    cpx.pixels[i] = newcolor
    i += 1
  
  time.sleep(0.25)