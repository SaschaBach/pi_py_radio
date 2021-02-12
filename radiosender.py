import time
import vlc

from myLogger import MyLogger

class Radiosender(object):
       
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.myLogger = MyLogger(self.__class__.__name__ + '[' + name + ']')

    def play(self):
        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.url)
        self.media.get_mrl()
        self.player.set_media(self.media)
        
        self.player.play()
        self.myLogger.info('play ' + self.url) 
                
    def stop(self):
        self.player.stop()
        self.myLogger.info('stop ' + self.url) 
