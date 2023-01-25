class Character:
    hp = 50

    def __init__(self, name):
        self.name = name


class Knight(Character):
    hp = 125
    item = ["sword"]


class Druid(Character):
    hp = 75
    item = ["wand"]