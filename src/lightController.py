
try: 
	from neopixel import *
	import time, threading
except Exception as err:
	print err

class LightController:
    def __init__(self):
        try:
			#LED strip configuration:
            self.LIGHTS_COUNT = 200	# Number of LED pixels used.
            self.LED_PIN = 18						# GPIO pin connected to the pixels.
            self.LED_FREQ_HZ = 800000					# LED signal frequency in hertz (usually 800khz)
            self.LED_DMA = 10							# DMA channel to use for generating signal (try 10) 
            self.LED_INVERT = False						# True to invert the signal (when using NPN transistor level shift)
            self.LED_BRIGHTNESS = 100                   # Set to 0 for darkest and 255 for brightest		
            self.LED_CHANNEL = 0						# set to '1' for GPIOs 13, 19, 41, 45 or 53
            self.LED_STRIP = ws.WS2811_STRIP_GRB	# Strip type and colour ordering
            self.strip = Adafruit_NeoPixel(200, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
            self.MAX_BRIGHTNESS = 255
            self.LED_LIGHT_DELAY = 0.05
            self.FLORIDA_GATORS_DELAY = 1.0
            self.CANDY_CANE_LENGTH = 5
            self.candyCaneLights = False
            self.strip.begin()
        except Exception as ex:
            print 'Error while initializing a LightController: ' + str(ex)

    def updateBrightness(self, brightnessPercentage):
        self.LED_BRIGHTNESS = self.MAX_BRIGHTNESS * brightnessPercentage
        self.strip = Adafruit_NeoPixel(200, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)
        self.strip.show()

    def getLedBrightness(self):
        return "{0:.0%}".format(1.0*self.LED_BRIGHTNESS/self.MAX_BRIGHTNESS)

    def stopLightThreads(self):
        self.stopCandyCaneLights()
        self.stopfloridaGatorsLights()

    def lightsOff(self):
        self.stopLightThreads()
        for light in range(0, self.LIGHTS_COUNT):
            self.strip.setPixelColor(light, 0)
        self.strip.show()

    def lightsWhite(self):
        self.stopLightThreads()
        for light in range(0, self.LIGHTS_COUNT):
            self.strip.setPixelColor(light, Color(255,255,255))
            self.strip.show()
            time.sleep(self.LED_LIGHT_DELAY)

    def lightsRed(self):
        self.stopLightThreads()
        for light in range(0, self.LIGHTS_COUNT):
            self.strip.setPixelColor(light, Color(255,0,0))
            self.strip.show()
            time.sleep(self.LED_LIGHT_DELAY)

    def lightsRainbow(self):
        self.stopLightThreads()
        for light in range(0, self.LIGHTS_COUNT):
            if 0 == light % 7:
                self.strip.setPixelColor(light, Color(255,0,0))
            if 1 == light % 7:
                self.strip.setPixelColor(light, Color(255,165,0))
            if 2 == light % 7:
                self.strip.setPixelColor(light, Color(255,255,0))
            if 3 == light % 7:
                self.strip.setPixelColor(light, Color(0,255,0))
            if 4 == light % 7:
                self.strip.setPixelColor(light, Color(0,0,255))
            if 5 == light % 7:
                self.strip.setPixelColor(light, Color(75,0,130))
            if 6 == light % 7:
                self.strip.setPixelColor(light, Color(128,0,128))
            self.strip.show()
            time.sleep(self.LED_LIGHT_DELAY)

    def lightsRedWhite(self):
        self.stopLightThreads()
        for light in range(0, self.LIGHTS_COUNT):
            if 0 == light % 5:
                self.strip.setPixelColor(light, Color(255,0,0))
            else:
                self.strip.setPixelColor(light, Color(255,255,255))
            self.strip.show()
            time.sleep(self.LED_LIGHT_DELAY)

    def lightsRedWhiteGreen(self):
        self.stopLightThreads()
        for light in range(0, self.LIGHTS_COUNT):
            if 0 == light % 4 or 2 == light % 4:
                self.strip.setPixelColor(light, Color(255,255,255))
            elif 1 == light % 4:
                self.strip.setPixelColor(light, Color(0,255,0))
            elif 3 == light % 4:
                self.strip.setPixelColor(light, Color(255,0,0))
            self.strip.show()
            time.sleep(self.LED_LIGHT_DELAY)

    def lightsCandyCane(self):
        index = 0
        offset = 0
        if not self.candyCaneLights:
            self.candyCaneLights = True
            while self.candyCaneLights:
                for light in range(0, index):
                    self.strip.setPixelColor(light*self.CANDY_CANE_LENGTH+offset-1, Color(255,255,255))
                self.strip.show()
                if 0 == offset % self.CANDY_CANE_LENGTH:
                    if index * self.CANDY_CANE_LENGTH + offset < self.LIGHTS_COUNT:
                        index += 1
                    offset = 0
                for light in range(0, index):
                    self.strip.setPixelColor(light*self.CANDY_CANE_LENGTH+offset, Color(255,0,0))
                self.strip.show()
                time.sleep(self.LED_LIGHT_DELAY)
                offset += 1

    def lightsFloridaGators(self):
        self.stopLightThreads()
        if self.floridaGatorsLights = False:
            self.floridaGatorsLights = True
            while self.floridaGatorsLights:
                self.alternatingFloridaGatorsLights()
                self.floridaGatorsBlueRibbon()
                self.floridaGatorsOrangeRibbon()
                self.floridaGatorsScatter()
                self.lightsOff()

    def alternatingFloridaGatorsLights(self): 
        while alternate < 60 and self.floridatGatorsLights:
            for light in range(0, self.LIGHTS_COUNT):
                if 0 == light % 4:
                    color = Color(255, 165, 0) if 0 == alternate % 2 else Color(0,0,255)
                    self.strip.setPixelColor(light, color)
                elif 2 == light % 4:
                    color = Color(255, 165, 0) if 1 == alternate % 2 else Color(0,0,255)
                    self.strip.setPixelColor(light, color)
                else:
                    self.strip.setPixelColor(light, Color(0,0,0))
            alternate += 1
            self.strip.show()
            time.sleep(self.FLORIDA_GATORS_DELAY)

    def floridaGatorsBlueRibbon(self):
        if self.floridatGatorsLights:
            for light in range(0, self.LIGHTS_COUNT):
                if 2 == light % 4:
                    self.strip.setPixelColor(light, Color(0,0,255))
                else:
                    self.strip.setPixelColor(light, Color(0,0,0))
            self.strip.show()
            time.sleep(self.FLORIDA_GATORS_DELAY)
            for light in range(0, self.LIGHTS_COUNT):
                if Color(0,0,255) == self.strip.getPixelColor(light):
                    self.strip.setPixelColor(light, Color(255,165,0))
                else:
                    self.strip.setPixelColor(light, Color(0,0,255))
                self.strip.show()
                time.sleep(self.LED_LIGHT_DELAY)

    def floridaGatorsOrangeRibbon(self):
        if self.floridatGatorsLights:
            for light in range(0, self.LIGHTS_COUNT):
                if 2 == light % 4:
                    self.strip.setPixelColor(light, Color(255,165,0))
                else:
                    self.strip.setPixelColor(light, Color(0,0,0))
            self.strip.show()
            time.sleep(self.FLORIDA_GATORS_DELAY)
            for light in range(0, self.LIGHTS_COUNT):
                if Color(255,165,0) == self.strip.getPixelColor(light):
                    self.strip.setPixelColor(light, Color(0,0,255))
                else:
                    self.strip.setPixelColor(light, Color(255,165,0))
                self.strip.show()
                time.sleep(self.LED_LIGHT_DELAY)

    def floridaGatorsScatter(self):
        numLightCycles = 0
        while numLightCycles < 60:
            for light in range(0, self.LIGHTS_COUNT):
                if 0 == light % 16 and 0 == numLightCycles % 2:
                    self.strip.setPixelColor(light, Color(255,165,0))
                elif 8 == light % 16 and 1 == numLightCycles % 2:
                    self.strip.setPixelColor(light, Color(0,0,255))
                else:
                    self.strip.setPixelColor(light, Color(0,0,0))
            self.strip.show()
            time.sleep(self.FLORIDA_GATORS_DELAY)
            numLightCycles += 1

        for light in range(0, self.LIGHTS_COUNT):
            if 0 == light % 2 and 0 == alternate % 2:
                self.strip.setPixelColor(light, Color(255,165,0))
            elif 1 == light % 2 and 0 == alternate % 1:
                self.strip.setPixelColor(light, Color(0,0,255))
            self.strip.show()
            time.sleep(self.LED_LIGHT_DELAY)
        
    def stopCandyCaneLights(self):
        self.candyCaneLights = False

    def stopfloridaGatorsLights(self):
        self.floridaGatorsLights = False
