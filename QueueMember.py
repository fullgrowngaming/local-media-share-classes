import pafy

class QueueMember:
    def __init__(self, username, bits, url):
        self.username = username
        self.bits = bits
        self.url = url
        try:
            self.pafy = pafy.new(self.url)
        except:
            self.pafy = None
        else:
            self.parsed_url = self.pafy.getbest().url
            self.video_length = self.pafy.length

    def __str__(self):
        return f'{self.username} {str(self.bits)} {pafy.new(self.url).title}'

