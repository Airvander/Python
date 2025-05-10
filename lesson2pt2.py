x = "1"  # this is a number in string format
y = 8
print(int(x) + y) ## this will convert the string to an int and add it to y
#print(x + y) ## this will not work because you cannot add a string and an int

x = 1.2
y = 8
print(x + y) #adding a float and an int

x = "1.2" # this is a number in string format
y = 8.5
print(float(x) + y) ## this will convert the string to a float and add it to y

x = 1.2
y = 8.5
print(f"The sum of {x} and {y} is {x + y}")
print(f"The sum of {x} + {y} = {x + y}") ## this will convert the float to a string and add it to y

#experiment with the following code this code will not work
#x = 1.2.4.6
#y = 8.5.6.7
#print(x + y)
#print(float(x) + float(y)) ## this will convert the string to a float and add it to y

ip1 = "1.2.4.6"
ip2 = "8.5.6.7"
print(f"ip address 1: {ip1} \nip address 2: {ip2}")

input1 = input("Enter first ip address: ")
input2 = input("Enter second ip address: ")
print(f"ip address 1: {input1} \nip address 2: {input2}")


######## the purpose of f-strings is to format the string and display the output in a readable format (it may contain ints, floats, strings, etc.) and turn them into strings