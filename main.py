import threading
import sys

from radiosenderProcess import RadiosenderProcess
from myLogger import MyLogger

myLogger = MyLogger('main')
myLogger.info('Starte Anwendung')

radiosenderProcess = RadiosenderProcess()

try:
   radiosenderThread = threading.Thread(target=radiosenderProcess.process, name="RadiosenderProcessThread")
   radiosenderThread.start()
except:
    e = sys.exc_info()[0]
    myLogger.error("Threads konnten nicht gestartet werden: %s" % e )    

# Todos:
# 1. RadiosenderSwitch in einen Thread auslagern. Beim Catch all geht es auf kein sender zurück
# 2. Herausfinden wie VLC die Lautstärke regelt

