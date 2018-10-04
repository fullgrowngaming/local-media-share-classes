import vlc
import pafy
import time

class MediaPlayer:
    def __init__(self):
        self.instance = self.create_player()

    def create_player(self):
        instance = vlc.Instance()
        player = instance.media_player_new()
        return (instance, player)

    def construct_url(self, url):
        if url == None:
            return None
        
        video = pafy.new(url)
        best = video.getbest()
        return best.url

    def play_video(self, duration, url):
        parsed_url = self.construct_url(url)

        if parsed_url != None:
            media = self.instance[0].media_new(parsed_url)
            media.get_mrl()
            self.instance[1].set_media(media)
            self.instance[1].play()
    
            end = time.time() + duration
    
            while True:
                if time.time() > end:
                    self.instance[1].stop()
                    break
                if input() == 'skip':
                    self.instance[1].stop()
                    break
