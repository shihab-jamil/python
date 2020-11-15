import random



guessNumber = int(input("Guess a number between 1~5: "))

randomNumber = random.randint(1,5)

if guessNumber == randomNumber:
    print("You have won the game!!!")

else:
    print("You loose...... The number was ",randomNumber)


