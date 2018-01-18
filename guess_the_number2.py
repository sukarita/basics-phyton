import random

print("Hello. What is your name? ")
name=input()

print("Well " + name + " I'm thinking of a number between 1 and 20.  Take a guess!!")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
	print("Take a guess")
	guess=int(input())

	if guess < secretNumber:
		print("Your guess is to low. Please try again")
	elif guess > secretNumber:
		print ("Your guess is too high. Please try again")
	else:	
		break

if guess == secretNumber:
	print("Good job " + name +  " You guess my number in " + str(guessesTaken) + " guesses")	