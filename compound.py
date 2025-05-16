"""input:
prompt user principal amount
get principal amount
prompt user annual nominal interest rate 
get annual nominal interest rate
prompt user number of time interest compounded
get number of time interest compounded
prompt user number of year
get numbner of year

process:
Final amount = principal amount * (1 + (interest rate / compound))**(compound*year)

output:
display final amount
print("The Final amount is", '${:0f}'.format(a))
"""
#This program is to help Tom compute the final amount for earning compound interest
p = int(input("Enter Principal amount: "))
r = float(input("Enter annual nominal interest [as a decimal]: "))
n = int(input("Enter Number of times the interest is compounded per year: "))
t = int(input("Enter number of years: "))
#Calculation for compound interest
a = p*(1+(r/n))**(n*t)
print("The Final amount is", '${:0f}'.format(a))
#Dollars and coin
'''print("The Final amount is", '${:.2f}'.format(a))'''
