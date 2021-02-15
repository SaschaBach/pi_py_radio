import time
import sys

from radiosender import Radiosender
from radiosenderSwitch import RadiosenderSwitch
from myLogger import MyLogger

myLogger = MyLogger('main')

myLogger.info('Starte Anwendung')

radiosenderSwitch = RadiosenderSwitch()

try:
    radiosenderFail = radiosenderSwitch.get_radiosender("Fail") 
    radiosenderFail.play()
    time.sleep(20)
    radiosenderFail.stop()
    time.sleep(20)
except: # catch *all* exceptions
    e = sys.exc_info()[0]
    myLogger.error(e.message)

radiosender2 = radiosenderSwitch.get_radiosender(radiosenderSwitch.radioBob) 
radiosender2.play()
time.sleep(20)
radiosender2.stop()
time.sleep(20)

radiosender3 = radiosenderSwitch.get_radiosender(radiosenderSwitch.hr3) 
radiosender3.play()
time.sleep(20)
radiosender3.stop()
time.sleep(20)

# Todos:
# 1. RadiosenderSwitch in einen Thread auslagern. Beim Catch all geht es auf kein sender zurück
# 2. Herausfinden wie VLC die Lautstärke regelt