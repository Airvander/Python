total_no_visitors = int(input("enter total numbers of visitors:"))
num_SCandPR = int(input("enter number of SC and PR:"))

num_others = total_no_visitors - num_SCandPR
 
if num_others :
    total_cost = num_others * 15
    print("total price of tickets is $" , '{}'.format(total_cost))
else :
    print('admission is free')
