import logging
import coloredlogs

# logging.basicConfig(level=logging.DEBUG,format='[%(threadName)s] %(asctime)s %(name)s %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

class MyLogger(object):

    def __init__(self, className):
        self.myLogger = logging.getLogger(className)
        coloredlogs.install(fmt='%(asctime)s,%(msecs)03d [%(threadName)s] %(name)s[%(process)d] %(levelname)s %(message)s', level='DEBUG', logger=self.myLogger)

    def info(self, message):       
        self.myLogger.info(message) 

    def error(self, message):       
        self.myLogger.error(message) 
