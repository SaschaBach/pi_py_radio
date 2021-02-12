import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

class MyLogger(object):

    def __init__(self, className):
        self.myLogger = logging.getLogger(className)

    def info(self, message):       
        self.myLogger.info(message) 