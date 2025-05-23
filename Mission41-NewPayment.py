#Programming I

#######################################
#             Mission 4.1             #
#    New payment amount for seniors   #
#######################################

#Background
#==========
#To support the government initiative to help seniors with their living expenses,
#all supermarkets in Singapore will give a 5% discount for seniors who are aged 60
#and above 
#
#Write a Python program to check whether a person is eligible for discount
#and if he is, then calculate the new amount he has to pay.
#
#The program is to prompt user for his age, and amount to pay 
#and check his eligibility and calculate the new amount to pay
#and display the original and new amounts to pay.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - age
#   - amount
#   - new_amount


#START CODING FROM HERE
#======================
age = int(input("please enter your age:"))
amount = float(input("please enter the amount:"))

# Prompt and accept data from user

#Calculate new_payment
def cal_new_payment(age, amount):

    if age >= 60:#Check if user is eligible for discount
        new_amount = amount * 0.95 #Calculate new payment amount
        print("original amount to pay is $", '{:.1f}'.format(amount))
        print("new amount to pay is $", '{:.1f}'.format(new_amount))  
        return new_amount #Do not remove this line
    
#Do not remove the next line
cal_new_payment(age, amount) 

#input 65,120 output 114
#input 70,200 output 190
