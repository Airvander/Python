#Programming I

#######################################
#            Mission 3.2              #
#   Calculate Daily Total Energy Cost #
#######################################

#Background
#==========
#The total energy cost is calculated using this formula: 
#Total Energy Cost ($) = Total Energy consumed (kW) x 0.2356

#Write a Python program that displays a table of energy in watts/hour
#for various appliances and prompt user to enter the daily hours for
#each appliance. The program then displays the table again with the
#daily hours and calculated value of the total daily energy cost.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - appliance_list
#   - hr_list
#   - hrs_input
#   - total_energy_cost

#START CODING FROM HERE
#======================

#Create a list named appliance_list with the 3 appliances
#shown in the screenshot in Coursemology
appliance_list = ['Electric Fan','Air con','Refigerator']
print('List of Electrical Appliances with Energy in Watts/Hr:')
print()
print('Name \t Energy(Watts/Hr)')
print("{}".format(appliance_list[0]), "\t 70")
print("{}".format(appliance_list[1]), "\t 1200")
print("{}".format(appliance_list[2]), "\t 200")
print()

#Prompt and obtain input for average daily consumption for appliances
#hrs_input = input("Enter hours daily for the above applicances separated by ';' :")

hrs_input = '5;4;24'


#Perform Calculation of Total Daily Energy Cost
def calculateEnergyCost(appliance_list,hrs_input):
    #Code to parse the input string in hrs_input (Hint: Use the split() function)
    hr_list = hrs_input.split(';')
    print('Name \t Energy(Watts/Hr)\t Daily Hrs used')
    print('Electri Fan \t 70 \t {}'.format(hr_list[0]))
    print('Air Con \t 1200 \t {}'.format(hr_list[1]))
    print('Refigerator \t 200 \t {}'.format(hr_list[2]))

#    print() #Modify to display list of appliances and daily hours used
    
    total_energy = 70/1000 * int(hr_list[0]) + 1200/1000 * int(hr_list[1]) + 200/1000 * int(hr_list[2]) #Calculate total energy of all appliances
    
    total_energy_cost = (total_energy) * 0.2356#Formula to calculate total energy cost
    
    print('Total daily energy consumed (kW):',total_energy) #Modify to display the daily energy consumed
    print('Total Daily energy cost ($)',total_energy_cost) #Modify to display the calculated total energy cost

    return total_energy_cost #Do not remove this line

    
#Do not remove the next line
calculateEnergyCost(appliance_list,hrs_input)

#input [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]],'5;4;24' output 2.34422
