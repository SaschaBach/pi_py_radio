import vlc

from myLogger import MyLogger

class Radiosender(object):
       
    def __init__(self, url, name):
        self.url = url
        self.name = name

        self.myLogger = MyLogger(self.__class__.__name__ + '[' + name + ']')

        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        
        # fuer mp3s
        self.media = self.instance.media_new(self.url)
        self.media.get_mrl()
        self.player = self.instance.media_player_new()
        self.player.set_media(self.media)

        # fuer listen
        self.media_list = self.instance.media_list_new([self.url])
        self.list_player = self.instance.media_list_player_new()
        self.list_player.set_media_list(self.media_list)

    def play(self):
        self.list_player.play()
        # self.player.play()
        self.myLogger.info("play %s" % self.url)    

                
    def stop(self):
        self.list_player.stop()
        # self.player.stop()
        self.myLogger.info("stop %s" % self.url)    
