months_left = int(input("enter number of month left before passport expired:"))
months_to_entry = int(input("enter number of month to entry:"))

if months_left > 6 and (months_left - months_to_entry) > 6:
    print("passport is valid for entry")
else :
    print("passport needs renewal")
