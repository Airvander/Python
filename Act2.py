import random
num1 = random.randint(0,100)
num2 = random.randint(0,100)

num = int(input("Enter the sum of {:d} and {:d}: ".format(num1,num2)))
if num == num1 + num2:
    print("Your answer is correct!")
else:
    print("Your answer is wrong..")
    print("The correct answer is {:d}.".format(num1 + num2))
