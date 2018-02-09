import random
gameActive = True
generatedNumber  = random.randint(1,100)
while gameActive:
    userInput = input("Please guess a number between 1 and 100: ")
    if userInput != generatedNumber:
        print ("Not Match")
    else:
        print ("Match!")
        contin = raw_input("Would you like to play again? Yes or No: ")
        if contin == 'yes' or 'Yes':
            generatedNumber  = random.randint(1,100)
            gameActive = True
        else:
            print(" Thank You for playing!!")
            gameActive = False
    

