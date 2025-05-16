#Programming I

#######################
#     Mission 5.1     #
#   Vitality Points   #
#######################

#Background
#==========
#To encourage their customers to exercise more, insurance companies are giving
#vouchers for the distances that customers had clocked in a week as follows:


######################################################
#     Distance (km)     #  Gift                      #
######################################################
#  Less than 25         #  $2 Popular eVoucher       #
#  25 <= distance < 50  #  $5 Cold Storage eVoucher  #
#  50 <= distance < 75  #  $10 Starbucks eVoucher    #
#  More than 75         #  $20 Subway eVoucher       #
######################################################


#Write a Python program to check and display the gift that customer will recieve.

#The program is to prompt user for the total distance he had travelled (by walking or running)
#in a week and check which gift he will get and display the information to him.

#The return value of the function is the eVoucher value (e.g., 2 for the Popular eVoucher)

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - distance
#   - gift
#   - value



#START CODING FROM HERE
#======================
distance = int(input("enter distance walking or running in km:",))
#Prompt user for the total distance travelled (either by walking or running).



#Check gifts to be given to customer
def check_gift(distance):

    if distance < 25: #Check gift to be given
        value = 2
        print('You have receive $' + "{}".format(value), 'Popular eVocher')
    elif distance >= 25 and distance < 50:
        value = 5
        print('You have receive $' + "{}".format(value), 'Cold Storage eVocher')    
    elif distance >= 50 and distance < 75:
        value = 10
        print('You have receive $' + "{}".format(value), 'Starbucks eVocher')
    elif distance >75:
        value = 20
        print('You have receive $' + "{}".format(value), 'Subway eVocher')    
            
    #Modify to display gift to be given
    
    return value #Do not remove this line

    
#Do not remove the next line
check_gift(distance)

#input 10 output 2
#input 25 output 5
#input 50 output 10
#input 76 output 20
