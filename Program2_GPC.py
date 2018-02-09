import random
gameActive = True
#this can be used to make sure the player isnt cheating
userNumber = input("Please give me a number to guess: ")
userInput = input("What is the maximum range, 1 to ___? ")
computerGuess = random.randint(1,userInput)
ceiling = 100
floor = 0
print "Is your number " + str(computerGuess)

while gameActive:
    comparison = raw_input("Tell me too high with >, too low with <, or y if I got it! \n")
    if(comparison == ">"): 
        ceiling = computerGuess
        computerGuess = (ceiling + floor)/2
        #computerGuess = (computerGuess-floor)/2
        #computerGuess = computerGuess + floor
        print(computerGuess)   
        continue      
    elif (comparison == "<"):
        floor=computerGuess
        computerGuess = ((ceiling+floor)/2)
        #computerGuess = computerGuess+floor
        print(computerGuess)
        continue
    elif (comparison == "y"):
        print("Thank You for playing!")
        gameActive = False
    else:
        print("Please enter an accepted input!!!")
        continue
    
    
