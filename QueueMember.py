import pafy

class QueueMember:
    def __init__(self, username, bits, url):
        self.username = username
        self.bits = bits
        self.url = url

        self.parsed_url = pafy.new(self.url).getbest().url

    def __str__(self):
        return f'{self.username} {str(self.bits)} {pafy.new(self.url).title}'