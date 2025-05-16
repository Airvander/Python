list1 = [ 1, 3, 5, 7, 9 ]
# define the function
def change(list):
    for i in range(len(list)):
        list[i] += 1

print(list1)
change(list1)  # call the function 
print(list1)
