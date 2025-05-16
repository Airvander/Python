interest = 1.05
item = float(input("Enter Purchase item prices :$"))
instal = int(input("Enter Number of payment instalments in months: "))

total = sub + interest
sub = item / instal

print(item)
print(format(sub, '.2dp'))
print(format(total, '.2dp'))
