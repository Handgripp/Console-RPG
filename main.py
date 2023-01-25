from character import *


def main():
    print("Hello in console-rpg, choose what you want to do")
    print("")
    print("New character = 1 ")
    print("Load old character = 2")
    while True:
        user_chose_main = input("Enter a number (1 or 2) ")
        if user_chose_main.isdigit():
            user_chose_main = int(user_chose_main)
            if user_chose_main == 1:
                new_character()
            if user_chose_main == 2:
                load_character()
            else:
                print("Enter again a number (1 or 2)")
        else:
            print("Enter again a number")


def load_character():
    print("No elo")
    menu()


def exp():
    print("exp")


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
            number_in_menu = int(number_in_menu)
            if number_in_menu == 1:
                print("You chose shop")
                shop()
            if number_in_menu == 2:
                print("You chose exp")
                exp()
            else:
                print("Enter again a number (1 or 2)")
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
            user_chose = int(user_chose)
            if user_chose > 0:
                if user_chose == 1:
                    char_knight = Knight(char_name)
                    print("You chose a knight, Hello", char_name)
                    menu()
                if user_chose == 2:
                    char_druid = Druid(char_name)
                    print("You chose a druid, Hello", char_name)
                    menu()
                else:
                    print("Enter again a number (1 or 2)")
        else:
            print("Enter again a number")


main()
