import time
import sys

from myLogger import MyLogger
from radiosenderSwitch import RadiosenderSwitch

class RadiosenderProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init RadiosenderProcess')
        self.radiosenderSwitch = RadiosenderSwitch()

    def process(self):
        count = 0
        # Das muss in einer Endlosschleife laufen
        while count < 2:
            count += 1

            time.sleep(5)

            try:
                # Hier muss irgendein Status zum aktuell gewählten Radiosender abgefragt werden. 
                radiosenderFail = self.radiosenderSwitch.get_radiosender("Fail") 
                radiosenderFail.play()
                time.sleep(20)
                radiosenderFail.stop()
                time.sleep(20)
            except: # catch *all* exceptions
                # Hier muss der Status auf Default gesetzt werden und dann muss es weiter gehen. 
                e = sys.exc_info()[0]
                self.myLogger.error(e.message)

            radiosender2 = self.radiosenderSwitch.get_radiosender(self.radiosenderSwitch.radioBob) 
            radiosender2.play()
            time.sleep(20)
            radiosender2.stop()
            time.sleep(20)

            radiosender3 = self.radiosenderSwitch.get_radiosender(self.radiosenderSwitch.hr3) 
            radiosender3.play()
            time.sleep(20)
            radiosender3.stop()
            time.sleep(20)
            