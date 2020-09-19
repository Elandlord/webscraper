from Helpers.Formatter import Formatter
from Models.SiegeWeapon import SiegeWeapon
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

content = Formatter.beautifyContent(response.content)

tables = content.findAll('table', attrs={'class':'wikitable'})

siege_units = []

for index, row in enumerate(tables):

    if(index == 0):
        tbody = row.find('tbody')
        trList = row.find_all('tr')

        for siege_unit in trList:
            fields = siege_unit.findAll('td')

            name = ""
            hp = ""

            for fieldIndex, field in enumerate(fields):

                # Siege weapon name
                if(fieldIndex == 0):
                    for linkIndex, link in enumerate(field.findAll('a')):
                        if(linkIndex != 0):
                            name = link.text.encode('ascii')

                # Siege weapon HP
                if (fieldIndex == 3):
                    hp = field.text.strip().encode('ascii')

            if len(name) > 0 and len(hp) > 0:
                siege_units.append(SiegeWeapon(name, hp))

siege_units = filter(None, siege_units)

for siege_unit in siege_units:
    print(siege_unit.name)