from myLogger import MyLogger
from radiosender import Radiosender

class RadiosenderSwitch(object):

    radio_aus = 'radio_aus'
    radiosender = 'radiosender'
    hr3 = 'HR3'
    radioBob = 'RadioBob'

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init RadioSwitch')

        self.radiosenderDict = {self.radioBob:Radiosender('http://streams.radiobob.de/100/mp3-192/streams.radiobob.de/play.m3u',self.radioBob), 
        self.hr3:Radiosender('http://metafiles.gl-systemhaus.de/hr/hr3_2.m3u',self.hr3)}

    def get_radiosender(self, name):
        self.myLogger.info("get_radiosender(%s)" % name)    


        try:
            radiosender = self.radiosenderDict[name]
        except KeyError:
            self.myLogger.error("Radiosender %s unbekannt." % name)
            return 

        return radiosender 

     

