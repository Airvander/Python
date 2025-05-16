age = int(input("please enter your age:"))
amount = float(input("please enter the amount:"))
new_amount = amount * 0.95

if age >= 60:
    print("original amount to pay is $", '{:.1f}'.format(amount))
    print("new amount to pay is $", '{:.1f}'.format(new_amount))
else:
    print("original amount to pay is $", '{:.1f}'.format(amount))
    print("new amount to pay is $", '{:.1f}'.format(amount))
