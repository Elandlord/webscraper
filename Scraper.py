from Sources.AoE import AoE
from Client import Client

class Scraper:

    client = Client

    def __init__(self, client):
        self.client = client

    def get(self, url):
        return self.client.get(url)


scraper = Scraper(Client())
full_url = "https://ageofempires.fandom.com/wiki/Siege_weapons_(Age_of_Empires_II)"
response = scraper.get(full_url)

siege_units = AoE.format(response.content)

siege_units = filter(None, siege_units)

for siege_unit in siege_units:
    print(siege_unit.name)