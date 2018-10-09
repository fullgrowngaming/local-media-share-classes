class QueueMember:
    def __init__(self, username, bits, url):
        self.username = username
        self.bits = bits
        self.url = url

    def __str__(self):
        return f'{self.username} {str(self.bits)} {self.url}'