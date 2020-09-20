from bs4 import BeautifulSoup

class Formatter:

    @staticmethod
    def stripEncode(string, encoding = 'ascii'):
        return string.strip().encode(encoding)

    @staticmethod
    def beautifyContent(content):
        return BeautifulSoup(content, features="html.parser")
