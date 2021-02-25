import threading
import sys
import redis
import time
import argparse
from termcolor import colored

from volumeWatcherProcess import VolumeWatcherProcess
from switchWatcherProcess import SwitchWatcherProcess
from dryModeProcess import DryModeProcess
from radioProcess import RadioProcess
from lightProcess import LightProcess
from radioSwitch import RadioSwitch
from myLogger import MyLogger

print("************************************")       
print("______ _  ______          _ _")       
print("| ___ (_) | ___ \        | (_)")      
print("| |_/ /_  | |_/ /__ _  __| |_  ___")  
print("|  __/| | |    // _` |/ _` | |/ _ \ ")
print("| |   | | | |\ \ (_| | (_| | | (_) |")
print("\_|   |_| \_| \_\__,_|\__,_|_|\___/ ")
print("************************************")
print(colored("Press Ctrl-C to skip","red"))
print("************************************")

# process cmd line args
parser = argparse.ArgumentParser(description='Start script for the radio application')
parser.add_argument("--logLevel", type=str, default='INFO')
parser.add_argument("--dryMode", type=bool, default=False)
args = parser.parse_args()
logLevel = args.logLevel
dryMode = args.dryMode
print('Arg[logLevel]=%s' % logLevel )
print('Arg[dryMode]=%s' % dryMode )
print("************************************")

# init and create the first logger
MyLogger.level = logLevel
myLogger = MyLogger('main')

# set start values
redisServer = redis.Redis(host='localhost', port=6379, db=0)
redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radio_off)

# start working with the threads
stop_event = threading.Event()
    
radioProcess = RadioProcess()
radio_thread = threading.Thread(target=radioProcess.process, name="RadioThread", args=(stop_event,))
radio_thread.start()
    
if dryMode:
    myLogger.info('DryMode Flag is activ')
    dryModeProcess = DryModeProcess()
    dryMode_thread = threading.Thread(target=dryModeProcess.process, name="DryModeThread", args=(stop_event,))
    dryMode_thread.start()  
else:
    switchWatcherProcess = SwitchWatcherProcess()
    switchWatcher_thread = threading.Thread(target=switchWatcherProcess.process, name="SwitchWatcherThread", args=(stop_event,))
    switchWatcher_thread.start()

lightProcess = LightProcess()
light_thread = threading.Thread(target=lightProcess.process, name="LightThread", args=(stop_event,))
light_thread.start()

volumeWatcherProcess = VolumeWatcherProcess()
volumeWatcher_thread = threading.Thread(target=volumeWatcherProcess.process, name="VolumeWatcherThread", args=(stop_event,))
volumeWatcher_thread.start()

try:
    stop_event.wait()  # wait forever but without blocking KeyboardInterrupt exceptions

except KeyboardInterrupt:   
    myLogger.info("Ctrl+C pressed...")
    stop_event.set()  # inform the child thread that it should exit
    sys.exit(1)

# Todos:
# 1. VLC auf PI auf Mono im Default umstellen
# 2. Lautstaerke regeln
# 3. Abstrakte Klasse fuer Prozesse
# 4. vlc output auf mono
# 5. Airplay


                                    
                                    

