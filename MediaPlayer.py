import vlc
import pafy
import time

class MediaPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def construct_url(self, url):
        if url == None:
            return None
        
        video = pafy.new(url)
        best = video.getbest()
        return best.url

    def play_video(self, duration, url):
        parsed_url = self.construct_url(url)

        if parsed_url != None:
            media = self.instance.media_new(parsed_url)
            media.get_mrl()
            self.player.set_media(media)
            self.player.play()
    
            end = time.time() + duration
    
            while True:
                if time.time() > end:
                    self.player.stop()
                    break
                if input() == 'skip':
                    self.player.stop()
                    break
