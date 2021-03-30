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
        current_light_state = False
        self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_off)

        while not stop_event.is_set():
            time.sleep(1)

            try:
                self.myLogger.debug("Check selected radiostation")
                selected_radiostation_name = self.redisServer.get(RadioSwitch.selected_radiostation)
                radiostation_name_decoded = selected_radiostation_name.decode('utf-8')

                turn_light_on = False
                if radiostation_name_decoded != RadioSwitch.radio_off:
                    turn_light_on = True

                if current_light_state == turn_light_on:
                    continue

                if turn_light_on:
                    self.myLogger.info("Switch on light and turn amp on")
                    self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_on)
                else:
                    self.myLogger.info("Switch off light and turn amp off")
                    self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_off)

                current_light_state = turn_light_on
                current_radiostation_name = radiostation_name_decoded

            except: # catch *all* exceptions
                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e )   

        self.myLogger.info("Stop event is set. Stop %s" % self.__class__.__name__)
        self.gpioController.call(GPIOController.gpio_led_3_3_v, GPIOController.gpio_off)
      