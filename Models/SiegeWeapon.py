class SiegeWeapon:

    name = ""
    hp = 0
    attack = 0
    armor = 0
    pierce_armor = 0
    weapon_range = 0
    rate_of_fire = 0
    line_of_sight = 0
    speed = 0
    food_cost = 0
    wood_cost = 0
    gold_cost = 0
    train_time_in_seconds = 0
    no_of_civs_with_access = 0

    def __init__(self, name, hp, attack, armor, pierce_armor, weapon_range, rate_of_fire, line_of_sight, speed, food_cost, wood_cost, gold_cost, train_time_in_seconds, no_of_civs_with_access):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.pierce_armor = pierce_armor
        self.weapon_range = weapon_range
        self.rate_of_fire = rate_of_fire
        self.line_of_sight = line_of_sight
        self.speed = speed
        self.food_cost = food_cost
        self.wood_cost = wood_cost
        self.gold_cost = gold_cost
        self.train_time_in_seconds = train_time_in_seconds
        self.gold_cost = gold_cost
        self.no_of_civs_with_access = no_of_civs_with_access

    @staticmethod
    def buildInsertQuery(siege_unit):
        return "INSERT INTO siege_weapons (%s) VALUES (%s)"

    @staticmethod
    def getKeys(siege_unit):
        return vars(siege_unit).keys()

    @staticmethod
    def getValues(siege_unit):
        return vars(siege_unit).values()