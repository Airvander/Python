item1 = float(input("Enter item 1 price:$ "))
item2 = float(input("Enter item 2 price:$ "))
item3 = float(input("Enter item 3 price:$ "))
item4 = float(input("Enter item 4 price:$ "))
item5 = float(input("Enter item 5 price:$ "))

sub = item1 + item2 + item3 +  item4 + item5
tax = sub * 0.07
total = sub + tax

print("Subtotal = $", sub)
print("Sales Tax = $", tax )
print("Total = $", total)
#five item, total sales, 7 percent 0.07, display subtotal, display sales tax, display total amount
