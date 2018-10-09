import vlc
import pafy
import time
from Settings import bits_per_second
from QueueMember import QueueMember
import threading

class MediaPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.play_queue = []

    def play_video(self):

        while self.play_queue:
            member = self.play_queue[0]
            media = self.instance.media_new(member.parsed_url)
            self.player.set_media(media)
            self.player.play()
            time.sleep(float(member.bits / bits_per_second))
            self.player.stop()
            self.play_queue.remove(member)


