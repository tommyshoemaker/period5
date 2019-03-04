import random
maxnum = int(input("What do you want the maximum number to be? "))
number = int(random.randint(0, maxnum))
guess = None
tries = 0
while guess != number:
    guess = int(input("Type in a number: "))
    if guess == number:
        print("You guessed the number in", tries, "tries! Thanks for playing.")
        exit()
    elif guess > number:
        print("Too high, guess lower.")
        tries += 1
    elif guess < number:
        print("Too low, guess higher.")
        tries += 1
    
