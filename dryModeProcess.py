import time
import sys
import redis

from myLogger import MyLogger
from radioSwitch import RadioSwitch

class DryModeProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init DryModeProcess')
        self.redisServer = redis.Redis(host='localhost', port=6379, db=0)

    def process(self, stop_event):
        count = 0

        # loop a couple of times for simulation
        while count < 5 and not stop_event.is_set():
            count += 1

            time.sleep(5)

            try:
                self.myLogger.info('Starte RadioBob')
                self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radioBob)

                time.sleep(10)

                self.myLogger.info('Starte hr3')
                self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.hr3)

                time.sleep(10)

            except: # catch *all* exceptions
                self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radio_off)    
                self.myLogger.debug("Set selected radiostation on default %s." % RadioSwitch.radio_off)

                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e )   

        self.myLogger.info("Stop event is set. Stop dry mode process.")      