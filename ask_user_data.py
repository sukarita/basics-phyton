#Ask user for name
name = input("What is your name?: ")


#Ask user for the age
age = input("How old are you? ")

#Ask user for city
city = input("What city do you live in? ")

#Ask user what they enjoy
hobbies = input("What are your hobbies?, What do you love doing? ")

#Create output text using placeholders to concatenate data
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, hobbies)

#Print output to screen
print(output)
