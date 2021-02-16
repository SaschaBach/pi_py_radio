import logging
import coloredlogs
from logging.handlers import RotatingFileHandler

# logging.basicConfig(level=logging.DEBUG,format='[%(threadName)s] %(asctime)s %(name)s %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

class MyLogger(object):

    level = "INFO"
    my_format = '%(asctime)s,%(msecs)03d [%(threadName)s] %(name)s[%(process)d] %(levelname)s %(message)s'

    def __init__(self, className):
        self.myLogger = logging.getLogger(className)
        
        handler = RotatingFileHandler('pi_py_radio.log', maxBytes=200000, backupCount=3)
        formatter = logging.Formatter(MyLogger.my_format)
        handler.setFormatter(formatter)
        self.myLogger.addHandler(handler)
        
        coloredlogs.install(fmt=MyLogger.my_format, level=MyLogger.level, logger=self.myLogger)

    def debug(self, message):
        self.myLogger.debug(message)

    def info(self, message):       
        self.myLogger.info(message) 

    def error(self, message):       
        self.myLogger.error(message) 
