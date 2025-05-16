import random
nos = random.randint(1,100)
print('Welcome to Number Guessing Game')
num = int(input('Try 1: Enter a number between 1 and 100 (or -1 to end): '))
correct = 1

while correct <=5:
    if num == nos:
        print("Bingo, you've got it right!")
        break
    
    elif num == -1:
        print("You've given up! The correct number is", nos)
        break
    
    elif num < nos:
        print('{} is too low.' .format(num))
    
    elif num > nos:
        print('{} is too high.'.format(num))
      
    if correct == 5:
        print('Game over. The correct answer is: ',nos)
        break
        
    correct += 1
    #num = int(input("Try "+str(correct)+": Guess again, enter a number between 1 and 100 (or -1 to end):"))
    num = int(input("Try {}: Guess again, enter a number between 1 and 100 (or -1 to end):".format(correct)))

print('Bye-bye!')
