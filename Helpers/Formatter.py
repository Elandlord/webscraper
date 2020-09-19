from bs4 import BeautifulSoup

class Formatter:

    @staticmethod
    def beautifyContent(content):
        soup = BeautifulSoup(content)
        return soup
