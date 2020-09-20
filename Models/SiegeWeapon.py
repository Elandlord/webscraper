class SiegeWeapon:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def buildInsertQuery(siege_unit):
        return "INSERT INTO siege_weapons (%s) VALUES (%s)"

    @staticmethod
    def getKeys(siege_unit):
        return vars(siege_unit).keys()

    @staticmethod
    def getValues(siege_unit):
        return vars(siege_unit).values()