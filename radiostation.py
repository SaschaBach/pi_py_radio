import vlc

from myLogger import MyLogger

class Radiostation(object):
       
    def __init__(self, url, name):
        self.url = url
        self.name = name

        self.myLogger = MyLogger(self.__class__.__name__ + '[' + name + ']')
        self.myLogger.info('Init Radiostation')

        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        
        # for single files
        self.media = self.instance.media_new(self.url)
        self.media.get_mrl()
        self.player = self.instance.media_player_new()
        self.player.set_media(self.media)

        # for lists
        self.media_list = self.instance.media_list_new([self.url])
        self.list_player = self.instance.media_list_player_new()
        self.list_player.set_media_list(self.media_list)

    def play(self):
        self.myLogger.debug("play %s" % self.url)    
        self.list_player.play() 
        # self.player.play()

                
    def stop(self):
        self.myLogger.debug("stop %s" % self.url)    
        self.list_player.stop()
        # self.player.stop()

    def set_volume(self, volume):
        self.myLogger.debug("audio_set_volume %s" % volume)    
        self.list_player.get_media_player().audio_set_volume(volume)

