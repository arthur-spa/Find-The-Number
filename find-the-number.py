import time
import random

print("Welcome to find a number !")
time.sleep(1)

def gameLoop():
    finded = False
    print("Let me think about a number...")
    toFind = random.randint(1, 100)
    print("The number I'm thinking is between 1 and 100")
    print("Try to find it !")
    time.sleep(1)

    while (finded == False):
        inputed = int(input("\nEnter a number beetwin 1 and 100 "))
        if (inputed == toFind):
            finded = True
            print("You find it !")
            break
        if (inputed > toFind):
            print("You're above !")
        else:
            print("You're under !")

gameLoop()

time.sleep(1)
replay = input("Want to play again ? (y/n) ")
if (replay == "y"):
    print("Let's go !")
    time.sleep(1)
    gameLoop()
else:
    print("Bye !")
