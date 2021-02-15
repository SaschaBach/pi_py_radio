import time
import sys
import redis

from myLogger import MyLogger
from radiosenderSwitch import RadiosenderSwitch

class RadiosenderProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init RadiosenderProcess')
        self.radiosenderSwitch = RadiosenderSwitch()

    def process(self):
        count = 0

        currentRadiosenderName = RadiosenderSwitch.radioBob
        self.radiosender = self.radiosenderSwitch.get_radiosender(currentRadiosenderName) 
        self.radiosender.play()

        # Das muss in einer Endlosschleife laufen
        while count < 5:
            count += 1

            time.sleep(10)

            try:
                redisServer = redis.Redis(host='localhost', port=6379, db=0)
                radiosenderName = redisServer.get(RadiosenderSwitch.radiosender)
                radiosenderNameDecoded = radiosenderName.decode('utf-8')
                self.myLogger.debug('Radiosender aus Redis %s' % radiosenderNameDecoded)

                self.myLogger.debug('currentRadiosenderName %s' % currentRadiosenderName)

                if currentRadiosenderName == radiosenderNameDecoded:
                    continue

                self.myLogger.info("Aktueller Radiosender gewechselt zu %s" % radiosenderNameDecoded)
                
                self.radiosender.stop()
                self.myLogger.debug("Aktueller Radiosender gestoppt %s " % self.radiosender.name)
                
                self.radiosender = self.radiosenderSwitch.get_radiosender(radiosenderNameDecoded)
                self.myLogger.debug("Aktueller Radiosender gewechselt %s " % self.radiosender.name)

                self.radiosender.play()
                currentRadiosenderName = radiosenderNameDecoded

            except: # catch *all* exceptions
                # Hier muss der Status auf Default gesetzt werden und dann muss es weiter gehen. 
                e = sys.exc_info()[0]
                self.myLogger.error("Fehler im Prozess: %s" % e )     