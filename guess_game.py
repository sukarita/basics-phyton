#Guess the number game
import random

print("Hello. What is your name?")
name = input()  #save the name in a variable

print("Well, " + name + ", I'm thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20) #including 20

#Loop up to certain number of times
for guessesTaken in range(1, 7):  #excluding 7
    print("Take a guess")
    guess = int(input())  #convert guess into an int

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is to high")
    else:  
        break  #This condition is for the correct guess!

if guess == secretNumber:
    print("Good job!!! " + name + " You guessed my number in " + str(guessesTaken) + " guesses")
    
print("Nope. The number I was thinking of was " + str(secretNumber))
