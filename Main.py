from TwitchConnection import TwitchConnection
from MediaPlayer import MediaPlayer
from QueueMember import QueueMember
from MessageParser import *
from Settings import NICK, CHANNEL
import threading

def main():
    read_buffer = ''
    while True:
        read_buffer = read_buffer + str(c.connection.recv(2048))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            if 'PING :tmi.twitch.tv' in line:
                c.pong()
            elif ' PRIVMSG #' in line:
                    print(f'{get_user(line)} cheered {bits_parse(line)} bits!')
                    if url_parse(line) != None:
                        player.play_queue.append(QueueMember(get_user(line), 5, url_parse(line)))


def play_video():
    while True:
        player.play_video()

c = TwitchConnection(NICK, CHANNEL)
player = MediaPlayer()

t1 = threading.Thread(target=play_video)

t1.start()
main()










            