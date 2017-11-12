#This program says hello and ask for my name & age

print("Hello World!")
print("What is your name?") #Ask for their name
myName = input()
print("Is good to meet you, " + myName)
print("The lenght of your name is: ")
print(len(myName))
print("What is your age: ") #Ask for their age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year")
