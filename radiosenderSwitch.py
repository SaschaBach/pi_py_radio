from myLogger import MyLogger
from radiosender import Radiosender

class RadiosenderSwitch(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init RadioSwitch')

        self.radiosenderDict = {'RadioBob':Radiosender('http://streams.radiobob.de/bob-live/mp3-192/mediaplayer','RadioBob'), 
        'HR3':Radiosender('http://hr-hr3-live.cast.addradio.de/hr/hr3/live/mp3/128/stream.mp3','HR3')}

    def get_radiosender(self, name):
        self.myLogger.info('get_radiosender(' + name + ')')

        return self.radiosenderDict[name]

     

