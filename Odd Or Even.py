"""
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""

num = int(input("Enter first number: "))
check = int(input("Enter second number: "))

if num % 2 == 0:
  print("The number you entered is EVEN.")
else:
  print("The number you entered is ODD.")

if num % 4 == 0:
  print("The number you entered is divisible by 4.")
else:
  print("The number you entered is not divisible by 4.")

if num % check == 0:
  print(str(num) + " divides evenly into " + str(check) )
else:
  print(str(num) + " not divides evenly into " + str(check) )
  
