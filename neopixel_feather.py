from machine import Pin
from neopixel import NeoPixel
pixel = NeoPixel(Pin(16, Pin.OUT), 1)
pixel[0] = (0, 255, 0)
pixel.write()

