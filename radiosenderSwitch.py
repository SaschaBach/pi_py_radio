from myLogger import MyLogger
from radiosender import Radiosender

class RadiosenderSwitch(object):

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init RadioSwitch')

        self.radiosenderDict = {'RadioBob':Radiosender('http://streams.radiobob.de/bob-live/mp3-192/mediaplayer','RadioBob'), 
        'HR3':Radiosender('http://metafiles.gl-systemhaus.de/hr/hr3_2.m3u','HR3')}

    def get_radiosender(self, name):
        self.myLogger.info('get_radiosender(' + name + ')')

        return self.radiosenderDict[name]

     

