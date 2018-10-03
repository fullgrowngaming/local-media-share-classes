import vlc
import pafy
import time

class MediaPlayer:
    def __init__(self, duration, url):
        self.duration = duration
        self.url = url
        self.parsed_url = self.construct_url(url)

    def construct_url(self, url):
        if url == None:
            return None
        
        video = pafy.new(url)
        best = video.getbest()
        return best.url

    def play_video(self):
        if self.parsed_url != None:
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(self.parsed_url)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
    
            end = time.time() + self.duration
    
            while True:
                if time.time() > end:
                    player.stop()
                    break
