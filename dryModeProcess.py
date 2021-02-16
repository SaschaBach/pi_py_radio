import time
import sys
import redis

from myLogger import MyLogger
from radiosenderSwitch import RadiosenderSwitch

class DryModeProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init DryModeProcess')

    def process(self):
        count = 0

        redisServer = redis.Redis(host='localhost', port=6379, db=0)

        # Das muss in einer Endlosschleife laufen
        while count < 5:
            count += 1

            time.sleep(10)

            try:
                self.myLogger.info('Starte RadioBob')
                redisServer.set(RadiosenderSwitch.radiosender, RadiosenderSwitch.radioBob)

                time.sleep(10)

                self.myLogger.info('Starte hr3')
                redisServer.set(RadiosenderSwitch.radiosender, RadiosenderSwitch.hr3)

                time.sleep(10)

            except: # catch *all* exceptions
                # Hier muss der Status auf Default gesetzt werden und dann muss es weiter gehen. 
                e = sys.exc_info()[0]
                self.myLogger.error("Fehler im Prozess: %s" % e )     