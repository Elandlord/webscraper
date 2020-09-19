from Helpers.Formatter import Formatter
from Models.SiegeWeapon import SiegeWeapon

class AoE:

    @staticmethod
    def format(content):
        data = []
        content = Formatter.beautifyContent(content)

        tables = content.findAll('table', attrs={'class': 'wikitable'})

        for index, row in enumerate(tables):

            if (index == 0):
                tbody = row.find('tbody')
                trList = row.find_all('tr')

                for siege_unit in trList:
                    fields = siege_unit.findAll('td')

                    name = ""
                    hp = ""

                    for fieldIndex, field in enumerate(fields):

                        # Siege weapon name
                        if (fieldIndex == 0):
                            for linkIndex, link in enumerate(field.findAll('a')):
                                if (linkIndex != 0):
                                    name = link.text.encode('ascii')

                        # Siege weapon HP
                        if (fieldIndex == 3):
                            hp = field.text.strip().encode('ascii')

                    if len(name) > 0 and len(hp) > 0:
                        data.append(SiegeWeapon(name, hp))

        return data