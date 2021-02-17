import sys
import redis
import time

from myLogger import MyLogger
from radioSwitch import RadioSwitch
from gpioController import GPIOController

class LightProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init LightProcess')
        self.redisServer = redis.Redis(host='localhost', port=6379, db=0)
        self.gpioController = GPIOController()

    def process(self, stop_event):
        # init with start value
        current_radiostation_name = RadioSwitch.radio_off
        self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_off)

        while not stop_event.is_set():
            time.sleep(1)

            try:
                self.myLogger.debug("Check selected radiostation")
                selected_radiostation_name = self.redisServer.get(RadioSwitch.selected_radiostation)
                radiostation_name_decoded = selected_radiostation_name.decode('utf-8')

                if current_radiostation_name == radiostation_name_decoded:
                    continue
                
                if radiostation_name_decoded == RadioSwitch.radio_off:
                    self.myLogger.debug("Switch off light")
                    self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_off)
                else:
                    self.myLogger.debug("Switch on light")
                    self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_on)

                current_radiostation_name = radiostation_name_decoded

            except: # catch *all* exceptions
                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e )   

        self.myLogger.info("Stop event is set. Stop light process.")
        self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_off)
      