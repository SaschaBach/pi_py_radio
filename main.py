import threading
import sys
import redis
import time

from radiosenderProcess import RadiosenderProcess
from radiosenderSwitch import RadiosenderSwitch
from myLogger import MyLogger

myLogger = MyLogger('main')
myLogger.info('Starte Anwendung')

radiosenderProcess = RadiosenderProcess()

try:
    radiosenderThread = threading.Thread(target=radiosenderProcess.process, name="RadiosenderProcessThread")
    radiosenderThread.start()
    time.sleep(10)

    redisServer = redis.Redis(host='localhost', port=6379, db=0)
    myLogger.info('Starte RadioBob')
    redisServer.set(RadiosenderSwitch.radiosender, RadiosenderSwitch.radioBob)

    time.sleep(10)

    myLogger.info('Starte hr3')
    redisServer.set(RadiosenderSwitch.radiosender, RadiosenderSwitch.hr3)

    time.sleep(10)

except:
    e = sys.exc_info()[0]
    myLogger.error("Threads konnten nicht gestartet werden: %s" % e )    

# Todos:
# 1. RadiosenderSwitch in einen Thread auslagern. Beim Catch all geht es auf kein sender zurück
# 2. Herausfinden wie VLC die Lautstärke regelt

