from TwitchConnection import TwitchConnection
from MediaPlayer import MediaPlayer
from MessageParser import *
from Settings import NICK, CHANNEL

c = TwitchConnection(NICK, CHANNEL)

read_buffer = ''

while True:
        read_buffer = read_buffer + str(c.connection.recv(1024))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            if 'PING :tmi.twitch.tv' in line:
                c.pong()
            elif ' PRIVMSG #' in line:
                if ';bits=' in line and bits_parse(line) != None:
                    print(f'{get_user(line)} cheered {bits_parse(line)} bits!')
                    media_player = MediaPlayer(bits_parse(line), url_parse(line))
                    media_player.play_video()



            