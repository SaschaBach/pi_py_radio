import time
import sys
import RPi.GPIO as GPIO

from myLogger import MyLogger

class GPIOController(object):

    gpio_off = GPIO.LOW
    gpio_on = GPIO.HIGH
    gpio_led_3_3_v = 22
    gpio_radio_bob_switch = 18 
    gpio_hr3_switch = 23
    gpio_free_station_switch = 24

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init GPIOController')

        # call GPIOS by Numbers
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio_led_3_3_v, GPIO.OUT)
            GPIO.setup(self.gpio_radio_bob_switch, GPIO.IN)
            GPIO.setup(self.gpio_free_station_switch, GPIO.IN)
            GPIO.setup(self.gpio_hr3_switch, GPIO.IN)
        except: # catch *all* exceptions
                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e )   

    def call(self, gpio_number, gpio_command):
        self.myLogger.debug('Call GPIO %s with %x' % (gpio_number, gpio_command))

        GPIO.output(gpio_number, gpio_command)

    def request(self, gpio_number):
        self.myLogger.debug('Request GPIO %s' % gpio_number)

        return GPIO.input(gpio_number)

