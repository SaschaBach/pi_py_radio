import threading

from radiosenderProcess import RadiosenderProcess
from myLogger import MyLogger

myLogger = MyLogger('main')
myLogger.info('Starte Anwendung')

radiosenderProcess = RadiosenderProcess()

try:
   radiosenderThread = threading.Thread(radiosenderProcess.process())
   radiosenderThread.start()
except:
    myLogger.error("Threads konnten nicht gestartet werden.")


# Todos:
# 1. RadiosenderSwitch in einen Thread auslagern. Beim Catch all geht es auf kein sender zurück
# 2. Herausfinden wie VLC die Lautstärke regelt