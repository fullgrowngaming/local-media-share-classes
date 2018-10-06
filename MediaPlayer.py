import vlc
import pafy
import time
import math
import threading


class MediaPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def play_video(self, duration, url):

        if url == None:
            return None

        parsed_url = pafy.new(url).getbest().url

        media = self.instance.media_new(parsed_url)
        self.player.set_media(media)
        self.player.play()
        time.sleep(duration)
        self.player.stop()

