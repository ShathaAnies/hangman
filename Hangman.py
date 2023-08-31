import random
from re import A
words= ["nawal", "shatha", "raeefah"]
choosenWord = random.choice(words)

guesses = ''

tries = 6

while tries > 0:         

    failed = 0             

    for char in choosenWord:      

        if char in guesses:    
    
            print (char,end=" "),    

        else:
    
            print ("_ ",end=""),     
       
            failed += 1    


    if failed == 0:        
        print (" You won :)")
        break            
    guess = input("guess a character:") 

    guesses += guess                    

    if guess not in choosenWord:  
 
        tries -= 1        
        if tries==0:
                   print("    +---+ \n    O   |\n   /|\  |\n   / \  |\n      ===  \n \n you Lose :( ")
        elif tries==5 :
                    print("false  \n    +---+ \n        |\n        |\n        |\n      ===  \n")
        elif tries==4 :
                    print("false  \n    +---+ \n    O   |\n    |   |\n        |\n      ===  \n")
        elif tries==3 :
                    print("false  \n    +---+ \n    O   |\n   /|   |\n        |\n      ===  \n")
        elif tries==2 :
                    print("false  \n    +---+ \n    O   |\n   /|\  |\n        |\n      ===  \n")
        elif tries==1 :
                    print("false  \n    +---+ \n    O   |\n   /|\  |\n   /    |\n      ===  \n")
        