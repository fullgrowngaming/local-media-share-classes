from TwitchConnection import TwitchConnection
from MediaPlayer import MediaPlayer
from QueueMember import QueueMember
from MessageParser import *
from Settings import NICK, CHANNEL

import threading
import os
import time

def quit_handler():
    while True:
        if input() == 'q' or input() == 'quit' or input() == 'exit':
            print('Exiting...')
            os._exit(0)
        time.sleep(1)

if __name__ == "__main__":
    read_buffer = ''
    c = TwitchConnection(NICK, CHANNEL)
    player = MediaPlayer()
    input_thread = threading.Thread(target=quit_handler, daemon=True)
    input_thread.start()

    while True:
        read_buffer = read_buffer + str(c.connection.recv(2048))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            if 'PING :tmi.twitch.tv' in line:
                c.pong()
            elif ';bits=' in line and bits_parse(line) != None:
                    print(f'{get_user(line)} cheered {bits_parse(line) bits}!')
                    if url_parse(line) != None:
                        print(f'{get_user(line)} shared a video!')
                        player.add_to_queue(QueueMember(get_user(line), bits_parse(line), url_parse(line)))













            