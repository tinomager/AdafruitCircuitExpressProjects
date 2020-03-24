"""Save your file as "code.py" or "main.py" to run on the actual device.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
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