class Codec:
    def __init__(self):
        
        self.store = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        v = hash(longUrl)
        self.store['http://tinyurl.com/' + str(v)] = longUrl
        return 'http://tinyurl.com/' + str(v)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
       
        return self.store[shortUrl]



class Codec:
    def __init__(self):
        self.lookup = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        n = len(self.lookup)
        self.lookup.append(longUrl)
        return "http://tinyurl.com/" + str(n)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s = int(shortUrl.split('/')[-1])
        return self.lookup[s]



class Codec:
    def __init__(self):
        self.encoding = {}
        self.decoding = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        prefix = 'http://'
        if longUrl.startswith('https://'):
            prefix = 'https://'
            
        shortUrl = prefix + 'tinyurl.com/' + str(len(self.encoding.keys()) + 1)
        self.encoding[longUrl] = shortUrl
        self.decoding[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoding[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))