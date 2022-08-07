"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

a , b = [2,3,4,5,9,23,46,78,98] , [2,4,6,43,46,75,98]
c = []

if len(a) >= len(b):
    for i in range(len(a)):
        if a[i] in  b:
            c.append(a[i])
else:
    for i in range(len(b)):
        if b[i] in a :
            c.append(b[i])
    
print(c)

                    
        
