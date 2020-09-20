from Helpers.Formatter import Formatter
from Models.SiegeWeapon import SiegeWeapon


class AoE:

    @staticmethod
    def insert(connection, siege_units):

        # Get a cursor
        cursor = connection.cursor()

        for siege_unit in siege_units:
            sql = SiegeWeapon.buildInsertQuery(siege_unit)

            placeholders = ', '.join(['%s'] * len(vars(siege_unit)))
            columns = ', '.join(SiegeWeapon.getKeys(siege_unit))
            values = SiegeWeapon.getValues(siege_unit)

            cursor.execute(sql % (columns, placeholders), values)
            connection.commit()

    @staticmethod
    def format(content):
        data = []
        content = Formatter.beautifyContent(content)

        tables = content.findAll('table', attrs={'class': 'wikitable'})

        siege_table = tables[0]

        tbody = siege_table.find('tbody')
        trList = siege_table.find_all('tr')

        for siege_unit in trList[1:-1]:
            fields = siege_unit.findAll('td')
            columns = [i.text for i in fields]

            args = {
                "name": Formatter.stripEncode(columns[0]),
                "hp": Formatter.stripEncode(columns[3]),
                "attack": Formatter.stripEncode(columns[4]),
                "armor": Formatter.stripEncode(columns[5]),
                "pierce_armor": Formatter.stripEncode(columns[6]),
                "weapon_range": Formatter.stripEncode(columns[7]),
                "rate_of_fire": Formatter.stripEncode(columns[8]),
                "line_of_sight": Formatter.stripEncode(columns[9]),
                "speed": Formatter.stripEncode(columns[10]),
                "food_cost": Formatter.stripEncode(columns[11]),
                "wood_cost": Formatter.stripEncode(columns[12]),
                "gold_cost": Formatter.stripEncode(columns[13]),
                "train_time_in_seconds": Formatter.stripEncode(columns[14]),
                "no_of_civs_with_access": Formatter.stripEncode(columns[15])
            }

            data.append(SiegeWeapon(**args))

        return data
