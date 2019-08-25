tempDict = {}
count = 0 
class Codec:
    def encode(self, longUrl):
        global count 
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tempDict[count] = longUrl
        count += 1
        return "http://tinyurl.com/" + str(count-1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        valArray = shortUrl.split("/")
        return tempDict[int(valArray[-1])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))