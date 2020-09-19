from Client import Client

class Scraper:

    client = Client

    def __init__(self, client):
        self.client = client

    def get(self, url):
        return self.client.get(url)


scraper = Scraper(Client())
fullUrl = "https://ageofempires.fandom.com/wiki/Siege_weapons_(Age_of_Empires_II)"
response = scraper.get(fullUrl)
print(response.text)