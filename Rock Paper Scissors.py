"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
"""
options = ["rock", "paper", "scissors"]

while True:
    
    play = input("Do you want play? :").lower()
    
    if play == "yes":
        
        user1 = input("user1: Rock or Paper or Scissors? :").lower()
        user2 = input("user2: Rock or Paper or Scissors? :").lower()
        
        if user1 == options[0] and user2 == options[0]:
            print("Draw.")
        
        elif user1 == options[1] and user2 == options[1]:
            print("Draw.")
        
        elif user1 == options[2] and user2 == options[2]:
            print("Draw.")
            
        elif user1 == options[0] and user2 == options[1]:
            print("user2 won.")
            
        elif user1 == options[0] and user2 == options[2]:
            print("user1 won.")
            
        elif user1 == options[1] and user2 == options[0]:
            print("user1 won.")
            
        elif user1 == options[1] and user2 == options[2]:
            print("user2 won.")
            
        elif user1 == options[2] and user2 == options[0]:
            print("user2 won.")
            
        elif user1 == options[2] and user2 == options[1]:
            print("user1 won.")
            
        else:
            print("Please enter a valid value.")


    elif play == "no":
        print("Logged out.")
        break        
    else:
        print("Please enter a valid value.")




    

    