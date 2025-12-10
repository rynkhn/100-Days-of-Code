print("Welcome to Tresure Island.\nYour mission is to find the treasure.")
choice = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\"\n")

if choice == "left":
    choice = input("You've come to a lake. There is an island in the middle of the lake.\n\tType \"wait\" to wait for a boat. Type \"swin\" to swim across.\n")
    if choice == "wait":
        choice = input("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which one do you choose?\n")
        if choice == "yellow":
            print("You found the treasure. You win")
        elif choice == "red":
            print("It's a room full of fire.\nGame Over.")
        elif choice == "blue":
            print("You enter a room of beasts.\nGame Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")