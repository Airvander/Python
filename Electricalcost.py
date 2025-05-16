

mthly_cost = input('Enter electrical costs($) for 3 months: ')

mthly_cost = mthly_cost.split(";")

total = float(mthly_cost[0])+float(mthly_cost[1])+float(mthly_cost[2])
average = total/3

print("average cost is: " ,average)


"""
Input:
prompt user for 3 values
get values
separate ";"
separated ";"

process:
calculate Total cost of 3 months
total = mthly_cost + mthly cost + mthly cost
average = total / 3

output:
display average cost
"""
