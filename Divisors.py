"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
"""
number = int(input("Enter a number:"))

a = []

b = 1

for i in range(number):
    if number % b == 0:
        a.append(b)
    b += 1
    
print(a)
