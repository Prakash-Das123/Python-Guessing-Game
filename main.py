# import the module
from random import *

# variables
cpu_number = randrange(100)
your_guess = 0
guesses = 0


def main_loop(guesses):
    while True:
        print("Take a guess")
        your_guess = int(input("> "))
        guesses += 1
        if your_guess == cpu_number:
            print("You got it in " + str(guesses) + " guesses!")
            break
        elif your_guess < cpu_number:
            print("Too Low")
        else:
            print("Too high")
        if guesses > 10:
            print("You used up all your guesses.")
            print("The number I was thinking of is " + str(cpu_number))
            break

print("I'm thinking of a number between 0 and 100")
main_loop(guesses)
print("Thanks For Playing!")
print("By Bisrut and Prakash")
