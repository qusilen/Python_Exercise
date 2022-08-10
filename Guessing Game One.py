"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

number_of_guesses = 1

a = random.randint(1, 9)



while True:
    
    b = int(input("Enter your guessed number: "))
    
    if b == a:
        print("Exactly right.")
        print("Number of guesses: " + str(number_of_guesses))
        number_of_guesses = 1
        c = input("If you want play again press ENTER or type 'exit'.:").lower()
        if c == "exit":
            break
        else:
            a = random.randint(1, 9)
            continue
            
        break
            
    elif b < a:
        print("Too low.")
        number_of_guesses += 1
        continue
    
    elif 9 > b > a:
        print("Too high.")
        number_of_guesses += 1
        continue
        
    elif b > 9 :
        print("Please enter valid value!")
        continue
    


   

    

    
    
    
        
    
    

