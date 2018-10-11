from TwitchConnection import TwitchConnection
from MediaPlayer import MediaPlayer
from QueueMember import QueueMember
from MessageParser import *
from Settings import NICK, CHANNEL

if __name__ == "__main__":
    read_buffer = ''
    c = TwitchConnection(NICK, CHANNEL)
    player = MediaPlayer()

    while True:
        read_buffer = read_buffer + str(c.connection.recv(2048))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            if 'PING :tmi.twitch.tv' in line:
                c.pong()
            elif ' PRIVMSG #' in line:
                    print(f'{get_user(line)} shared a song!')
                    if url_parse(line) != None:
                        player.add_to_queue(QueueMember(get_user(line), 100, url_parse(line)))









            