import threading
import sys
import redis
import time
import argparse

from dryModeProcess import DryModeProcess
from radiosenderProcess import RadiosenderProcess
from radiosenderSwitch import RadiosenderSwitch
from myLogger import MyLogger

myLogger = MyLogger('main')
myLogger.info('Starte Anwendung')

parser = argparse.ArgumentParser(description='Start Skript für das Radio')
parser.add_argument("--logLevel", type=str, default='INFO')
parser.add_argument("--dryMode", type=bool, default=False)

args = parser.parse_args()

logLevel = args.logLevel
dryMode = args.dryMode
myLogger.debug('Arg[logLevel]=%s' % logLevel )
myLogger.debug('Arg[dryMode]=%s' % dryMode )

# Setze Startwerte
redisServer = redis.Redis(host='localhost', port=6379, db=0)
redisServer.set(RadiosenderSwitch.radiosender, RadiosenderSwitch.radio_aus)

try:
    radiosenderProcess = RadiosenderProcess()
    radiosenderThread = threading.Thread(target=radiosenderProcess.process, name="RadiosenderProcessThread")
    radiosenderThread.start()
    
    if dryMode:
        myLogger.info('DryMode Flag aktiv')
        dryModeProcess = DryModeProcess()
        dryModeThread = threading.Thread(target=dryModeProcess.process, name="DryModeProcessThread")
        dryModeThread.start()
    
    time.sleep(30)

except:
    e = sys.exc_info()[0]
    myLogger.error("Threads konnten nicht gestartet werden: %s" % e )    

# Todos:
# 1. RadiosenderSwitch in einen Thread auslagern. Beim Catch all geht es auf kein sender zurück
# 2. Herausfinden wie VLC die Lautstärke regelt
# 3. Abstrakte Klasse für die Hintergrund Prozesse die process() mit exception handling implementiert
# 4. schönes startbild
# 5. Stoppe Skript bei Tastendruck
# 6. Loglevel vom Start verarbeiten

