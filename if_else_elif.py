#Flow Control Statements If - Else - Elif

print("Enter a name ")
name=input()
if name != "":
    print("Thank you for entering your name")
else:
    print("You did not enter a name")


#The order of the elif statement does matter. The execution enter the first True condition the rest would be ignored

name = "Chris"
age = 300

if name == "Alice":  #Condition is checked
    print("Hi Alice")
elif age < 12:
    print("You are not Alice, kiddo.")
elif age > 200:
    print("Unlike you Alice is not an undead, inmortal vampire!") #True condition
elif age >100:
    print("You are not Alice, grannie.")




