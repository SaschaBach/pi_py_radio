import threading
import sys
import redis
import time
import argparse
from termcolor import colored

from dryModeProcess import DryModeProcess
from radioProcess import RadioProcess
from radioSwitch import RadioSwitch
from myLogger import MyLogger

def print_startscreen():
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

print_startscreen()

myLogger = MyLogger('main')

parser = argparse.ArgumentParser(description='Start Skript für das Radio')
parser.add_argument("--logLevel", type=str, default='INFO')
parser.add_argument("--dryMode", type=bool, default=False)
args = parser.parse_args()
logLevel = args.logLevel
dryMode = args.dryMode
myLogger.debug('Arg[logLevel]=%s' % logLevel )
myLogger.debug('Arg[dryMode]=%s' % dryMode )

# set start values
redisServer = redis.Redis(host='localhost', port=6379, db=0)
redisServer.set(RadioSwitch.selected_radiostation, RadioSwitch.radio_off)

try:
    stop_event = threading.Event()
    
    radioProcess = RadioProcess()
    radio_thread = threading.Thread(target=radioProcess.process, name="RadioThread", args=(stop_event,))
    radio_thread.start()
    
    if dryMode:
        myLogger.info('DryMode Flag is activ')
        dryModeProcess = DryModeProcess()
        dryMode_thread = threading.Thread(target=dryModeProcess.process, name="DryModeThread", args=(stop_event,))
        dryMode_thread.start()  

    stop_event.wait()  # wait forever but without blocking KeyboardInterrupt exceptions

    while True:
        time.sleep(60)
        myLogger.debug("Still alive.")

except KeyboardInterrupt:   
    myLogger.info("Ctrl+C pressed...")
    stop_event.set()  # inform the child thread that it should exit
    sys.exit(1)

# Todos:
# 1. RadiosenderSwitch in einen Thread auslagern. Beim Catch all geht es auf kein sender zurück
# 2. Herausfinden wie VLC die Lautstärke regelt
# 3. Abstrakte Klasse für die Hintergrund Prozesse die process() mit exception handling implementiert
# 4. schönes startbild
# 5. Stoppe Skript bei Tastendruck
# 6. Loglevel vom Start verarbeiten
# 7. In File loggen. 


                                    
                                    

