l = int(input("enter loan amount:"))
a = int(input("enter annual income:"))
c = int(input("enter current loans:"))
s = int(input("enter total savings:"))
y = int(input("enter years to pay back loan:"))

r = (l+c)/(s+a*y)

print("your interest rate is,", '{:.1f}'.format(r)+ "%")
