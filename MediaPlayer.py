import vlc
import pafy
import time
from Settings import bits_per_second
from QueueMember import QueueMember

class MediaPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.play_queue = []

    def play_video(self):

        if not self.play_queue:
            return None

        for member in self.play_queue:
            print(member)
            if member.url == None:
                self.play_queue.remove(member)
                return None

            parsed_url = pafy.new(member.url).getbest().url

            media = self.instance.media_new(parsed_url)
            self.player.set_media(media)
            self.player.play()
            time.sleep(float(member.bits / bits_per_second))
            self.player.stop()
            self.play_queue.remove(member)


