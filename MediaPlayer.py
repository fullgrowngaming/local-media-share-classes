import vlc
import pafy
import time
import threading
from Settings import bits_per_second
from QueueMember import QueueMember

class MediaPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.play_queue = []
        self.play_thread = threading.Thread(target=self.play_video)
        self.play_thread.start()

    def add_to_queue(self, QueueMember):
        self.play_queue.append(QueueMember)

    def play_video(self):
        while True: #this outer loop exists for multithreading purposees
            while self.play_queue:
                member = self.play_queue[0]
                if self.play_queue[0].pafy == None: #sloppy way of handling invalid video IDs
                    self.play_queue.remove(member)
                    break
                media = self.instance.media_new(member.parsed_url)
                self.player.set_media(media)
                duration = min(self.play_queue[0].video_length, self.play_queue[0].bits)
                self.player.play()
                time.sleep(float(duration / bits_per_second))
                self.player.stop()
                self.play_queue.remove(member)


