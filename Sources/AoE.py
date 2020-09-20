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

            name = columns[0].strip().encode('ascii')
            hp = columns[3].strip().encode('ascii')
            attack = columns[4].strip().encode('ascii')
            armor = columns[5].strip().encode('ascii')
            pierce_armor = columns[6].strip().encode('ascii')
            weapon_range = columns[7].strip().encode('ascii')
            rate_of_fire = columns[8].strip().encode('ascii')
            line_of_sight = columns[9].strip().encode('ascii')
            speed = columns[10].strip().encode('ascii')
            food_cost = columns[11].strip().encode('ascii')
            wood_cost = columns[12].strip().encode('ascii')
            gold_cost = columns[13].strip().encode('ascii')
            train_time_in_seconds = columns[14].strip().encode('ascii')
            no_of_civs_with_access = columns[15].strip().encode('ascii')

            if len(name) > 0:
                data.append(SiegeWeapon(name, hp, attack, armor, pierce_armor, weapon_range, rate_of_fire, line_of_sight, speed, food_cost, wood_cost, gold_cost, train_time_in_seconds, no_of_civs_with_access))

        return data