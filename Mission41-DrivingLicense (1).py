#Programming I

##################################
#           Mission 4.1          #
#   Driving License Eligiblity   #
##################################

#Background
#==========
#In Singapore to apply for a driving license, one must be at least 18 years old

#Write a Python program to check whether a person is eligible to apply for a
#driving test.
#The program is to prompt user for his age,
#and display his eligibility.

#Return the boolean True if the person is eligible.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - age


#START CODING FROM HERE
#======================
#age = int(input("please enter your age "))
# Prompt and accept data from user

#Check Eligibility
def check_eligibility(age):

    if age >= 18:
        print("you eligible for drving test")
        return True
    else :
        print("you not eligible for driving test")
                #return #Return True if user is eligible

    
#Do not remove the next line
check_eligibility(age) 

#input 25 output True
#input 17 (no output)
