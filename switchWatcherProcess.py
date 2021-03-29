import sys
import redis
import time

from myLogger import MyLogger
from gpioController import GPIOController
from radioSwitch import RadioSwitch

class SwitchWatcherProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init SwitchWatcherProcess')
        self.redisServer = redis.Redis(host='localhost', port=6379, db=0)
        self.gpioController = GPIOController()

    def process(self, stop_event):

        while not stop_event.is_set():
            time.sleep(1)

            try:
                gpio_radio_bob = self.gpioController.request(GPIOController.gpio_radio_bob_switch)
                self.myLogger.debug("State of RadioBob switch: %s" % gpio_radio_bob)

                gpio_radio_hr3 = self.gpioController.request(GPIOController.gpio_hr3_switch)
                self.myLogger.debug("State of HR3 switch: %s" % gpio_radio_hr3)

                gpio_free_station = self.gpioController.request(GPIOController.gpio_free_station_switch)
                self.myLogger.debug("State of free station switch: %s" % gpio_free_station)

                if gpio_radio_bob == 1:
                    self.myLogger.debug("Switch to RadioBob")
                    self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radioBob)
                    continue

                if gpio_free_station == 1:
                    self.myLogger.debug("Switch to AirPlay Mode")
                    self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.airplay)
                    continue

                self.myLogger.debug("No switch is pressed.")        
                self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radio_off)
                    
            except: # catch *all* exceptions
                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e )   

        self.myLogger.info("Stop event is set. Stop %s" % self.__class__.__name__)
      