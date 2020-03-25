"""
Turn the circuit into a flashlight
Use Button A to make the flashlight brighter
Use Button B to make the flashlight darker
"""

# import CPX library
from adafruit_circuitplayground.express import cpx
import time

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
cpx.pixels.brightness = 0.0
brightness = 0.0

while True:
  if cpx.button_a:
    brightness += 0.1
    time.sleep(0.25)
  
  if cpx.button_b:
    brightness -= 0.1
    time.sleep(0.25)

  if brightness > 1.0:
    brightness = 1.0

  if brightness < 0.0:
    brightness = 0.0
  
  cpx.pixels.brightness = brightness
