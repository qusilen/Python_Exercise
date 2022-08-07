"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

word = input("Enter a word: ")

s = word[::-1]

if s == word:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
    
    
