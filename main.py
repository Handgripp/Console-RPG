import random

from character import *

import sqlite3

current_character = ""
name_of_class = ItemKnight
item_axe = Axe()
item_jagged = JaggedSword()
db = sqlite3.connect("characters.db")
cursor = db.cursor()
cursor.execute(''' CREATE TABLE if not exists characters 
(id INTEGER PRIMARY KEY, name TEXT, class TEXT, hp INTEGER, item TEXT, coins INTEGER, exp INTEGER, lvl INTEGER)''')
cursor.execute(''' CREATE TABLE if not exists item_specification 
(item TEXT, class TEXT, price INTEGER, min_dmg INTEGER, max_dmg INTEGER, UNIQUE(item, class, price, min_dmg, max_dmg))''')

cursor.execute(f'''INSERT OR IGNORE INTO item_specification (item, class, price, min_dmg, max_dmg) 
                values ("{item_axe.name}", "{name_of_class.classes}", "{item_axe.price}", 
                "{item_axe.min_dmg}", "{item_axe.max_dmg}")''')
cursor.execute(f'''INSERT OR IGNORE INTO item_specification (item, class, price, min_dmg, max_dmg) 
                values ("{item_jagged.name}", "{name_of_class.classes}", "{item_jagged.price}", 
                "{item_jagged.min_dmg}", "{item_jagged.max_dmg}")''')
db.commit()


def main():
    global current_character
    cursor.execute("SELECT name FROM characters")
    names_from_db = cursor.fetchall()
    names = ""
    for i in names_from_db:
        names += str(i)

    print("Hello in console-rpg, choose what you want to do\n")
    print("New character = 1 ")
    print("Load old character = 2")
    while True:
        user_chose_main = input("Enter a number (1 or 2) ")
        if user_chose_main.isdigit():
            if user_chose_main == "1":
                new_character()
            if user_chose_main == "2":
                while True:
                    show_characters()
                    current_character = input("Enter a name of character ").capitalize()
                    load_character(current_character)
                    if current_character in names:
                        menu()
        else:
            print("Enter again a number")


def show_characters():
    cursor.execute(f"SELECT name, class, hp, item, coins, lvl FROM characters")
    names = cursor.fetchall()
    for i in names:
        print("Name:", i[0], "|", "class:", i[1], "|", "hp:", i[2], "|",
              "item:", i[3], "|", "coins:", i[4], "|", "lvl:", i[5], "|", "\n")


def load_character(name_of_character):
    cursor.execute(
        f"SELECT id, name, class, hp, item, coins, exp, lvl FROM characters WHERE name='{name_of_character}'")
    rows = cursor.fetchall()
    if rows:
        print("")
    return rows


def detail_of_loaded_character():
    global current_character
    actual_item = ""
    name_of_character = ""
    hp_char = 0
    coins = 0
    classes = ""
    exp_char = 0
    lvl = 0
    loaded_char = load_character(current_character)
    for i in loaded_char:
        name_of_character += i[1]
        classes += i[2]
        hp_char += int(i[3])
        actual_item += i[4]
        coins += int(i[5])
        exp_char += int(i[6])
        lvl += int(i[7])
    return name_of_character, classes, hp_char, actual_item, coins, exp_char, lvl


def exp():
    hits = load_hits_item()
    details = detail_of_loaded_character()
    name_of_character = details[0]
    hp_char = details[2]
    actual_item = details[3]
    coins = details[4]
    exp_char = details[5]
    lvl = details[6]
    min_dmg = hits[0]
    max_dmg = hits[1]
    monster = Monster()
    monster_med = MonsterMed()
    monster_high = MonsterHigh()
    while hp_char >= 0 or monster.hp >= 0 or monster_med.hp >= 0 or monster_high.hp >= 0:
        if monster.lvl <= lvl < monster_med.lvl:
            hp_char -= random.randint(monster.min_hits, monster.max_hits)
            monster.hp -= random.randint(min_dmg, max_dmg)
        if lvl > monster_med.lvl:
            if lvl <= monster_high.lvl:
                hp_char -= random.randint(monster_med.min_hits, monster_med.max_hits)
                monster_med.hp -= random.randint(min_dmg, max_dmg)
        if lvl >= monster_high.lvl:
            hp_char -= random.randint(monster_high.min_hits, monster_high.max_hits)
            monster_high.hp -= random.randint(min_dmg, max_dmg)

        if hp_char <= 0:
            print("You lose")
            print("Your hp after fight ", hp_char)
            coins += 0
            update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)
            menu()

        if monster.hp <= 0:
            print("You win")
            print("Your hp after fight ", hp_char)
            coins += Monster.coins
            exp_char += monster.exp
            print("You collect", Monster.coins, "coins")
            print("Now you have", coins, "coins")
            update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)
            lvl_up()
            menu()
        if monster_med.hp <= 0:
            print("You win")
            print("Your hp after fight ", hp_char)
            coins += MonsterMed.coins
            exp_char += monster_med.exp
            print("You collect", MonsterMed.coins, "coins")
            print("Now you have", coins, "coins")
            update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)
            lvl_up()
            menu()
        if monster_high.hp <= 0:
            print("You win")
            print("Your hp after fight ", hp_char)
            coins += MonsterHigh.coins
            exp_char += monster_high.exp
            print("You collect", MonsterHigh.coins, "coins")
            print("Now you have", coins, "coins")
            update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)
            lvl_up()
            menu()


def lvl_up():
    details = detail_of_loaded_character()
    name_of_character = details[0]
    hp_char = details[2]
    actual_item = details[3]
    coins = details[4]
    exp_char = details[5]
    lvl = details[6]
    if exp_char >= (100 * lvl):
        lvl += 1
        exp_char = 0
        update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)


def update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl):
    cursor.execute(f"UPDATE characters SET hp = {hp_char} WHERE name='{name_of_character}'")
    cursor.execute(f"UPDATE characters SET coins = {coins} WHERE name='{name_of_character}'")
    cursor.execute(f"UPDATE characters SET item = '{actual_item}' WHERE name='{name_of_character}'")
    cursor.execute(f"UPDATE characters SET exp = '{exp_char}' WHERE name='{name_of_character}'")
    cursor.execute(f"UPDATE characters SET lvl = '{lvl}' WHERE name='{name_of_character}'")
    db.commit()


def load_hits_item():
    loaded_char = load_character(current_character)
    item_to_load = ""
    name_of_character = ""
    for i in loaded_char:
        item_to_load += i[4]
        name_of_character += i[1]
    cursor.execute(f"SELECT min_dmg, max_dmg FROM item_specification WHERE item='{item_to_load}'")
    rows = cursor.fetchall()
    min_dmg = 0
    max_dmg = 0
    for x in rows:
        min_dmg = x[0]
        max_dmg = x[1]
    return min_dmg, max_dmg


def shop():
    details = detail_of_loaded_character()
    name_of_character = details[0]
    classes = details[1]
    hp_char = details[2]
    actual_item = details[3]
    coins = details[4]
    exp_char = details[5]
    lvl = details[6]
    print("What you want to buy? Potions or Items? (Potions = 1, Items = 2)")
    user_chose = int(input("Enter a number "))
    if user_chose == 1:
        potions = Potions()
        print("The red potion will heal you for", potions.red_pot, "hp")
        while True:
            try:
                user_chose_pot = str(input("Enter name of pot to buy (red) "))
                if user_chose_pot == "red" and coins >= potions.price:
                    hp_char += potions.red_pot
                    coins -= potions.price
                    update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)
                    print("Your hp after heal", hp_char)
                    print("Your coins after buy", coins)
                    print("Succes")
                    menu()
            except:
                print("Invalid name")

    if user_chose == 2:

        items = Shop()
        print("This is items for", classes)
        if classes == "Knight":
            while True:
                try:
                    print(items.items_knight[0], "price =", items.price[0], items.items_knight[1], "price =",
                          items.price[1])
                    user_chose_items = str(input("Enter a name of item "))
                    if user_chose_items == items.items_knight[0] and coins >= items.price[0]:
                        coins -= items.price[0]
                        actual_item = items.items_knight[0]
                        print("Your coins after buy", coins)
                        update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)
                        menu()
                    if user_chose_items == items.items_knight[1] and coins >= items.price[1]:
                        coins -= items.price[1]
                        actual_item = items.items_knight[1]
                        print("Your coins after buy", coins)
                        update_char(hp_char, name_of_character, coins, actual_item, exp_char, lvl)
                        menu()
                except:
                    print("Invalid name")


def menu():
    print()
    print("Choose what you want to do next")
    print("Go to shop - chose 1")
    print("Go to exp - chose 2")
    while True:
        number_in_menu = input("Enter a number (1 or 2) ")
        if number_in_menu.isdigit():
            if number_in_menu == "1":
                print("You chose shop")
                shop()
            if number_in_menu == "2":
                print("You chose exp")
                exp()
        else:
            print("Enter again a number")


def new_character():
    global current_character
    print()
    print("Here you will create a new character, but first enter a name for your character")
    current_character = input("Enter name ").capitalize()
    print("Ok, next choose your class")
    print("Knight = 1")
    print("Druid = 2")
    while True:
        user_chose = input("Enter a number (1 or 2) ")
        if user_chose.isdigit():
            if user_chose > "0":
                if user_chose == "1":
                    char_knight = Knight(current_character)
                    print("You chose a knight, Hello", char_knight.name)
                    cursor.execute(f'''insert into characters (name, class, hp, item, coins, exp, lvl) 
                    values ("{char_knight.name}", "Knight", "{char_knight.hp}", "Sword", 10, 
                    "{char_knight.exp}", "{char_knight.lvl}")''')
                    db.commit()
                    menu()
                if user_chose == "2":
                    char_druid = Druid(current_character)
                    print("You chose a druid, Hello", char_druid.name)
                    cursor.execute(f'''insert into characters (name, class, hp, item, coins) 
                    values ("{char_druid.name}", "Druid", "{char_druid.hp}", "Wand", 10, 
                    "{char_druid.exp}", "{char_druid.lvl}")''')
                    db.commit()
                    menu()
        else:
            print("Enter again a number")


main()

db.close()
