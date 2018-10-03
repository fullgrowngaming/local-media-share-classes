import socket

from User import User
from Settings import HOST, PORT, PASS, NICK

class TwitchConnection:
    def __init__(self, user, channel):
        self.user = User(NICK, PASS)
        self.channel = channel
        self.connection = socket.socket()

        self.connection.connect((HOST, PORT))

        # IRC specific protocol
        self.connection.send(f'PASS {self.user.password}\r\n'.encode('utf-8'))
        self.connection.send(f'NICK {self.user.username}\r\n'.encode('utf-8'))
        self.connection.send(f'JOIN #{channel}\r\n'.encode('utf-8'))

        # request Twitch specific information (subs, cheers, badges, etc.)
        self.connection.send('CAP REQ :twitch.tv/tags\r\n'.encode('utf-8'))
        self.connection.send('CAP REQ :twitch.tv/membership\r\n'.encode('utf-8'))
        self.connection.send('CAP REQ :twitch.tv/commands\r\n'.encode('utf-8'))
        
        TwitchConnection.join_room(self)

    def join_room(self):
        loading = True
        while loading:
            read_buffer = str(self.connection.recv(1024))
            temp = read_buffer.split('\\r\\n')
            read_buffer = temp.pop()

            for line in temp:
                if "End of" in line:
                    print(f'{self.user.username} connected to: {self.channel}')
                    loading = False
                    
        TwitchConnection.send_message(self, f'Joined channel: {self.channel}')

        
    def send_message(self, message):
        temp_message = "PRIVMSG #" + self.channel + " :" + message
        self.connection.send((temp_message + "\r\n").encode('utf-8'))


    def pong(self):
        self.connection.send(('PONG :tmi.twitch.tv' + '\r\n').encode('utf-8'))
        print('Sent: PONG')



        




