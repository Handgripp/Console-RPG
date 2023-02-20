import random


class Character:
    hp = 50
    exp = 0
    lvl = 0

    def __init__(self, name):
        self.name = name


class Knight(Character):
    hp = 125
    item = "Sword"
    hits = 5
    exp = 0
    lvl = 0


class Druid(Character):
    hp = 75
    item = "Wand"
    hits = 25
    exp = 0
    lvl = 0


class Monster:
    lvl = 0
    hp = 125
    min_hits = 5
    max_hits = 10
    coins = 15
    exp = random.randint(15, 25)


class MonsterMed:
    lvl = 5
    hp = 150
    min_hits = 10
    max_hits = 15
    coins = 25
    exp = random.randint(35, 55)


class MonsterHigh:
    lvl = 10
    hp = 175
    min_hits = 20
    max_hits = 25
    coins = 35
    exp = random.randint(60, 85)


class Shop:
    items_knight = ["Axe", "Jagged Sword"]
    price = [0, 5]
    dmg_knight = [10, 15]
    items_druid = ["Wand of Vortex", "Wand of Inferno"]


class ItemKnight:
    classes = "Knight"


class Axe(ItemKnight):
    name = "Axe"
    price = 0
    min_dmg = 10
    max_dmg = 20


class JaggedSword(ItemKnight):
    name = "Jagged Sword"
    price = 5
    min_dmg = 15
    max_dmg = 25


class Potions:
    red_pot = 100
    price = 0
