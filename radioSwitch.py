from myLogger import MyLogger
from radiostation import Radiostation

class RadioSwitch(object):

    radio_off = 'radio_off'
    selected_radiostation = 'selected_radiostation'
    hr3 = 'HR3'
    radioBob = 'RadioBob'

    def __init__(self):
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init RadioSwitch')

        self.radiostationDict = {self.radioBob:Radiostation('http://streams.radiobob.de/100/mp3-192/streams.radiobob.de/play.m3u',self.radioBob), 
        self.hr3:Radiostation('http://metafiles.gl-systemhaus.de/hr/hr3_2.m3u',self.hr3)}

    def get_radiostation(self, name):
        self.myLogger.info("get_radiostation(%s)" % name)    

        try:
            radiostation = self.radiostationDict[name]
        except KeyError:
            self.myLogger.error("Unknown radiostation: %s." % name)
            return 

        return radiostation 

     

