"""
TODO desc.
"""

# import CPX library
from adafruit_circuitplayground.express import cpx
import time
from random import seed
from random import randint

def check_index(i):
  if i >= 0 and i <= 9:
    return True
  else:
    return False

seed(1)
cpx.pixels.brightness = 0.3

while True:
  # set new colors
  colors = []
  colors.append((randint(0, 255), randint(0, 255), randint(0,255)))
  colors.append((randint(0, 255), randint(0, 255), randint(0,255)))
  colors.append((randint(0, 255), randint(0, 255), randint(0,255)))
  
  # Move 1 - from right to left
  i = -3
  while i <= 14:
    j = 0
    while j <= 2:
      if check_index(i-j):
        cpx.pixels[i-j] = colors[j]
      j += 1
    
    #also check the pixel whether it has to be switched of
    if check_index(i-j):
      cpx.pixels[i-j] = (0, 0, 0)

    i += 1
    time.sleep(0.1)

  #short wait between the moves
  time.sleep(0.25)

  # Move 2 - from left to right
  i = 12
  while i >= -5:
    j = 0
    while j <= 2:
      if check_index(i+j):
        cpx.pixels[i+j] = colors[j]
      j += 1
    
    #also check the pixel whether it has to be switched of
    if check_index(i+j):
      cpx.pixels[i+j] = (0, 0, 0)

    i -= 1
    time.sleep(0.1)

  #short wait between the moves
  time.sleep(0.25)