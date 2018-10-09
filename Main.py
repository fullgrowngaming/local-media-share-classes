from TwitchConnection import TwitchConnection
from MediaPlayer import MediaPlayer
from QueueMember import QueueMember
from MessageParser import *
from Settings import NICK, CHANNEL
import threading

c = TwitchConnection(NICK, CHANNEL)
player = MediaPlayer()

read_buffer = ''

while True:
        read_buffer = read_buffer + str(c.connection.recv(1024))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            print(line)
            if 'PING :tmi.twitch.tv' in line:
                c.pong()
            elif ' PRIVMSG #' in line:
                #if ';bits=' in line and bits_parse(line) != None:
                #currently just testing without bits, hi geek
                #this basically works, I just need to implement actual threading
                    #print(f'{get_user(line)} cheered {bits_parse(line)} bits!')
                    player.play_queue.append(QueueMember(get_user(line), 10, url_parse(line)))
                    player.play_video()



            