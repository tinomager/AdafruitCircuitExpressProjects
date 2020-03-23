"""Save your file as "code.py" or "main.py" to run on the actual device.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground.express import cpx
import time

def calc_color(counter):
  r = 0
  g = 0
  b = 0
  
  if counter <= 255:
    r = 255 - counter
    g = counter
    b = 0
  elif counter <= 511:
    r = 0
    g = 255 - (counter - 256)
    b = (counter - 256)
  else:
    r = (counter - 512)
    g = 0
    b = 255 - (counter - 512)
  
  return r,g,b

cpx.pixels[0] = (255, 255, 255)
cpx.pixels[1] = (255, 255, 255)
cpx.pixels[2] = (255, 255, 255)
cpx.pixels[3] = (255, 255, 255)
cpx.pixels[4] = (255, 255, 255)
cpx.pixels[5] = (255, 255, 255)
cpx.pixels[6] = (255, 255, 255)
cpx.pixels[7] = (255, 255, 255)
cpx.pixels[8] = (255, 255, 255)
cpx.pixels[9] = (255, 255, 255)
cpx.pixels.brightness = 0.1
counter = 0

while True:
  r,g,b = calc_color(counter)
  cpx.pixels[0] = (r, g, b)
  cpx.pixels[1] = (r, g, b)
  cpx.pixels[2] = (r, g, b)
  cpx.pixels[3] = (r, g, b)
  cpx.pixels[4] = (r, g, b)
  cpx.pixels[5] = (r, g, b)
  cpx.pixels[6] = (r, g, b)
  cpx.pixels[7] = (r, g, b)
  cpx.pixels[8] = (r, g, b)
  cpx.pixels[9] = (r, g, b)

  counter += 1

  if counter == 768:
    counter = 0
