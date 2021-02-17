import time
import sys
import redis

from myLogger import MyLogger
from radioSwitch import RadioSwitch

class RadioProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init RadioProcess')
        self.radioSwitch = RadioSwitch()
        self.redisServer = redis.Redis(host='localhost', port=6379, db=0)

        # nur zum initialisieren. Todo: huebsch machen.
        self.current_radiostation = self.radioSwitch.get_radiostation(RadioSwitch.radioBob) 

    def process(self, stop_event):
        current_radiostation_name = RadioSwitch.radio_off

        while not stop_event.is_set():
            time.sleep(1)

            try:
                selected_radiostation_name = self.redisServer.get(RadioSwitch.selected_radiostation)
                radiostation_name_decoded = selected_radiostation_name.decode('utf-8')
                
                self.myLogger.debug('Selected Radiostation: %s.' % radiostation_name_decoded)
                self.myLogger.debug('Current Radiostation: %s.' % current_radiostation_name)

                if current_radiostation_name == radiostation_name_decoded:
                    continue

                self.myLogger.info("Change Radiostation to %s." % radiostation_name_decoded)
                
                self.current_radiostation.stop()
                self.myLogger.debug("Stop current radiostation %s ." % self.current_radiostation.name)

                if radiostation_name_decoded != RadioSwitch.radio_off:                
                    self.current_radiostation = self.radioSwitch.get_radiostation(radiostation_name_decoded)
                    self.current_radiostation.play()

                current_radiostation_name = radiostation_name_decoded

            except: # catch *all* exceptions
                self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radio_off)    
                self.myLogger.debug("Set selected radiostation on default %s." % RadioSwitch.radio_off)

                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e ) 

        self.myLogger.info("Stop event is set. Stop radio process.")    
        self.current_radiostation.stop()