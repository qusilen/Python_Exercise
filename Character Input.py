"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).
"""

year = 2022
name = input("Please enter your name:")
age = input("Please enter your age:")


year_of_birth = year - int(age)

turn100yo = year_of_birth + 100

print("Your name: " + name)
print("Your age: " + age)
print("The year you turn 100: " + str(turn100yo))






