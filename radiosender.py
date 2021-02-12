import vlc, time 

class Radiosender(object):
    
    def __init__(self, url, name) :
        self.url = url
        self.name = name
        self.instance = vlc.Instance('--input-repeat=-1','--fullscreen')

    def play(self):
        media = self.instance.media_new(self.url)
        media.get_mrl()
        
        player = self.instance.media_player_new()
        player.set_media(media)
        player.play()