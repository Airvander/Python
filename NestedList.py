##list1 = [1,3,5,7,9]
##list2 = [2,4,6,8,10]
##main_list = [list1,list2]
##
####for item in main_list:
####    for i in range(len(item)):
####        item[i] += 1
##
##print(main_list[1][4])
##print(list1)
##print(main_list[1])
##print(list2)
##




list1 = ['a,1', 'b,3', 'c,5', 'd,7', 'e,9']
list2 = ['z,2', 'y,4', 'x,6', 'w,8', 'v,10']
main_list = [list1, list2]
# display the total and average

total = 0
for item in main_list:
    for s in item:
        n = s.split(",")
        total += int(n[1])
print(total)
        
    
