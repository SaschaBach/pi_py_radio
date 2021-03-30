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
        current_volume = 0

        while not stop_event.is_set():
            time.sleep(1)

            try:
                selected_radiostation_name = self.redisServer.get(RadioSwitch.selected_radiostation).decode('utf-8')

                self.myLogger.debug('Selected Radiostation: %s.' % selected_radiostation_name)
                self.myLogger.debug('Current Radiostation: %s.' % current_radiostation_name)

                selected_volume = int(self.redisServer.get(RadioSwitch.selected_volume).decode('utf-8'))
                
                if current_volume != selected_volume:
                    self.myLogger.debug('Change Volume: %s.' % selected_volume)
                    self.current_radiostation.set_volume(selected_volume)
                    current_volume = selected_volume

                if current_radiostation_name != selected_radiostation_name:
                    
                    if selected_radiostation_name == RadioSwitch.radio_off or selected_radiostation_name == RadioSwitch.airplay:       
                        self.myLogger.info("Stop Radio. Selected station %s." % selected_radiostation_name)
                        self.current_radiostation.stop()
                        self.myLogger.debug("Stop current radiostation %s ." % self.current_radiostation.name)
                    else:
                        self.myLogger.info("Change Radiostation to %s." % selected_radiostation_name)

                        self.myLogger.debug("Stop current radiostation %s ." % self.current_radiostation.name)
                        self.current_radiostation.stop()

                        self.current_radiostation = self.radioSwitch.get_radiostation(selected_radiostation_name)
                    
                        self.myLogger.debug("Play selected radiostation %s ." % self.current_radiostation.name)
                        self.current_radiostation.play()

                    current_radiostation_name = selected_radiostation_name
                
            except: # catch *all* exceptions
                self.redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radio_off)    
                self.myLogger.debug("Set selected radiostation on default %s." % RadioSwitch.radio_off)

                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e ) 

        self.myLogger.info("Stop event is set. Stop %s" % self.__class__.__name__)
        self.current_radiostation.stop()