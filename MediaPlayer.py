import vlc
import pafy
import time

class MediaPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def play_video(self, duration, url):

        if url == None:
            return None

        parsed_url = pafy.new(url).getbest().url

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
