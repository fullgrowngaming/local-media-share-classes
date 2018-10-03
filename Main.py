from TwitchConnection import TwitchConnection
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
            else:
                print(line)
            