import random

moods = ["happy", "hungry", "sleepy", "bored"]

pet_name = input("Name your pet: ")
mood = "happy"
print("welcome {pet_name} is {mood}.")

while True:
    print("\nWhat would you like to do?")
    print("1. feed")
    print("2. sleep")
    print("3. play")
    print("4. quit")

    choice = int(input("> "))
    if choice == 1:
        print("you give {pet_name} a hotdog")
