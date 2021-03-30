import sys
import redis
import time

from myLogger import MyLogger
from gpioController import GPIOController
from MCP3008Controller import MCP3008Controller
from radioSwitch import RadioSwitch

class VolumeWatcherProcess(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init VolumeWatcherProcess')
        self.redisServer = redis.Redis(host='localhost', port=6379, db=0)
        self.mcp3008Controller = MCP3008Controller()

    def process(self, stop_event):

        while not stop_event.is_set():
            time.sleep(1)

            try:
                value = self.mcp3008Controller.read(channel=7)
                self.myLogger.debug("voltage current: %.2f" % (value))

                if value > 4000:
                    self.redisServer.set(RadioSwitch.selected_volume, 100)
                    continue
                
                if value > 3000:
                    self.redisServer.set(RadioSwitch.selected_volume, 90)
                    continue
                   
                if value > 2000:
                    self.redisServer.set(RadioSwitch.selected_volume, 80)
                    continue

                if value > 1500:
                    self.redisServer.set(RadioSwitch.selected_volume, 70)
                    continue

                if value > 800:
                    self.redisServer.set(RadioSwitch.selected_volume, 60)
                    continue

                if value > 500:
                    self.redisServer.set(RadioSwitch.selected_volume, 50)
                    continue

                if value > 300:
                    self.redisServer.set(RadioSwitch.selected_volume, 40)
                    continue

                if value > 100:
                    self.redisServer.set(RadioSwitch.selected_volume, 30)
                    continue

                if value > 50:
                    self.redisServer.set(RadioSwitch.selected_volume, 20)
                    continue     

                if value > 10:
                    self.redisServer.set(RadioSwitch.selected_volume, 10)
                    continue      

                if value < 10:
                    self.redisServer.set(RadioSwitch.selected_volume, 0)
                    continue
                    
            except: # catch *all* exceptions
                e = sys.exc_info()[0]
                self.myLogger.error("Error: %s" % e )   

        self.myLogger.info("Stop event is set. Stop %s" % self.__class__.__name__)
       