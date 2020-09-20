from bs4 import BeautifulSoup

class Formatter:

    @staticmethod
    def beautifyContent(content):
        soup = BeautifulSoup(content, features="html.parser")
        return soup
