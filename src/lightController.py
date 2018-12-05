
try: 
	from neopixel import *
	import time, threading
except Exception as err:
	print err

class LightController:
	def __init__(self):
		try:
			#LED strip configuration:
			self.LIGHTS_COUNT = 300	# Number of LED pixels used.
			self.LED_PIN = 18						# GPIO pin connected to the pixels.
			self.LED_FREQ_HZ = 800000					# LED signal frequency in hertz (usually 800khz)
			self.LED_DMA = 10							# DMA channel to use for generating signal (try 10)
			self.LED_INVERT = False						# True to invert the signal (when using NPN transistor level shift)
			self.LED_BRIGHTNESS = 255					# Set to 0 for darkest and 255 for brightest
			self.LED_CHANNEL = 0						# set to '1' for GPIOs 13, 19, 41, 45 or 53
			self.LED_STRIP = ws.WS2811_STRIP_GRB	# Strip type and colour ordering
			self.strip = Adafruit_NeoPixel(200, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
			self.interval = 0.2
            self.strip.begin()
		except Exception as ex:
			logging.error('Error while initializing a LightController: ' + ex)

	def lightsOff(self):
		for light in range(0, self.LIGHTS_COUNT):
			self.strip.setPixelColor(light, 0)
		self.strip.show()

	def lightsWhite(self):
		for light in range(0, self.LIGHTS_COUNT):
			self.strip.setPixelColor(light, Color(255,255,255))
		    self.strip.show()
            time.sleep(self.interval)

	def lightsRed(self):
		for light in range(0, self.LIGHTS_COUNT):
			self.strip.setPixelColor(light, Color(255,0,0))
		    self.strip.show()
            time.sleep(self.interval)

	def lightsRainbow(self):
		for light in range(0, self.LIGHTS_COUNT):
            if 0 == self.LIGHTS_COUNT % 7:
                self.strip.setPixelColor(light, Color(255,0,0))
            if 1 == self.LIGHTS_COUNT % 7:
                self.strip.setPixelColor(light, Color(255,165,0))
            if 2 == self.LIGHTS_COUNT % 7:
                self.strip.setPixelColor(light, Color(255,255,0))
            if 3 == self.LIGHTS_COUNT % 7:
                self.strip.setPixelColor(light, Color(0,255,0))
            if 4 == self.LIGHTS_COUNT % 7:
                self.strip.setPixelColor(light, Color(0,0,255))
            if 5 == self.LIGHTS_COUNT % 7:
                self.strip.setPixelColor(light, Color(75,0,130))
            if 6 == self.LIGHTS_COUNT % 7:
                self.strip.setPixelColor(light, Color(128,0,128))
            self.strip.show()
            time.sleep(self.interval)

	def lightsRedWhite(self):
		for light in range(0, self.LIGHTS_COUNT):
            if 0 == self.LIGHTS_COUNT % 5:
			    self.strip.setPixelColor(light, Color(255,0,0))
            else:
                self.strip.setPixelColor(light, Color(255,255,255))
		    self.strip.show()
            time.sleep(self.interval)

	def lightsRedWhiteGreen(self):
		for light in range(0, self.LIGHTS_COUNT):
            if 0 == self.LIGHTS_COUNT % 2:
			    self.strip.setPixelColor(light, Color(255,255,255))
            elif 1 == self.LIGHTS_COUNT % 5:
                self.strip.setPixelColor(light, Color(0,255,0))
            else 3 == self.LIGHTS_COUNT % 5:
                self.strip.setPixelColor(light, Color(255,0,0))
		    self.strip.show()
            time.sleep(self.interval)

    

