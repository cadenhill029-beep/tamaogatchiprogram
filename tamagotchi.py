import random

moods = ["happy", "hungry", "sleepy", "bored"]

pet_name = input("Name your pet: ")
mood = "happy"
print("welcome {pet_name} is {mood}.")

while True:
    print("What would you like to do?")
    print("1. feed")
    print("2. sleep")
    print("3. play")
    print("4. quit")

    choice = int(input("> "))
    if choice == 1:
        print("you give {pet_name} a hotdog")
    elif choice == "3":
        print("you play with {pet_name}.")
        mood = random.choice(moods)
        print("{pet_name} is now {mood}")
    elif choice == "2":
        print("you let {pet_name} sleep.")
        mood = random.choice(moods)
        print("{pet_name} is now {mood}!")

    elif choice == "4":
        print("farewell {pet_name} s hall miss you")
        break