from character import *

char_name = input("Enter name ")


def exp():
    print("exp")


def shop():
    print("You want to buy something?")


def main():
    print()
    print("Choose what you want to do next")
    print("Go to shop - chose 1")
    print("Go to exp - chose 2")
    number_in_menu = int(input("Enter a number "))
    if number_in_menu == 1:
        print("You chose shop")
        shop()
    if number_in_menu == 2:
        print("You chose exp")
        exp()


print()
print("Choose your character")
print("Knight = 1")
print("Druid = 2")
user_chose = int(input("Enter a number "))

if user_chose > 0:
    if user_chose == 1:
        char_knight = Knight(char_name)
        print("You chose a knight, Hello", char_name)
        main()
    if user_chose == 2:
        char_druid = Druid(char_name)
        print("You chose a druid, Hello", char_name)
        main()
