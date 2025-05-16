"""
input: 
prompt user watt > get watt
prompt user hours > get hours

process:
consumption = (Power rating [Watts]* hours per day)/1000
cost = consumption * Electricity tariff

output:
display total cost of monthly electricity consumption
print("total cost of monthly electricity consumption is, ", ({:5f}))
"""
#This program is to calculate the total cost of electrical consumption
power_rating = float(input("Enter Power rating [Watts] of device: "))
hours = float(input("Enter Number of hours use per day: "))
#calculate the total cost of monthly electrical consumption 
consumption = power_rating * hours/1000
cost = consumption * 0.2156
#Display the total cost of electrical consumption
print("The calculated energy cost value is $" + '{:0.5f}'.format(cost))
