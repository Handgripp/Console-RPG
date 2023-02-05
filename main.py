from character import *

import sqlite3

current_character = ""

db = sqlite3.connect("characters.db")
cursor = db.cursor()
cursor.execute(''' CREATE TABLE if not exists characters 
(id INTEGER PRIMARY KEY, name TEXT, class TEXT, hp INTEGER, item TEXT)''')


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
    cursor.execute("SELECT name, class FROM characters")
    names = cursor.fetchall()
    print(names)


def load_character(name_of_character):
    cursor.execute(f"SELECT id, name, class, hp, item FROM characters WHERE name='{name_of_character}'")
    rows = cursor.fetchall()
    if rows:
        print("Succes")
    return rows


def exp():
    pedal = load_character(current_character)
    print(pedal)


def shop():
    print("You want to buy something?")


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
    print()
    print("Here you will create a new character, but first enter a name for your character")
    char_name = input("Enter name ")
    print("Ok, next choose your class")
    print("Knight = 1")
    print("Druid = 2")
    while True:
        user_chose = input("Enter a number (1 or 2) ")
        if user_chose.isdigit():
            if user_chose > "0":
                if user_chose == "1":
                    char_knight = Knight(char_name)
                    print("You chose a knight, Hello", char_knight.name)
                    cursor.execute(f'''insert into characters (name, class, hp, item) 
                    values ("{char_knight.name}", "Knight", "{char_knight.hp}", "{char_knight.item}")''')
                    db.commit()
                    menu()
                if user_chose == "2":
                    char_druid = Druid(char_name)
                    print("You chose a druid, Hello", char_druid.name)
                    cursor.execute(f'''insert into characters (name, class, hp, item) 
                    values ("{char_druid.name}", "Druid", "{char_druid.hp}", "{char_druid.item}")''')
                    db.commit()
                    menu()
        else:
            print("Enter again a number")


main()

db.close()
