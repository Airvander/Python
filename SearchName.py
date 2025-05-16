nameList = ["Tom", "Joe", "Mary", "John", "Bob", "Jane"]

name=input('Enter name to search :' )

position = nameList.index(name) #index is number of names

print('Name {} is found in postion {} in the name list.' .format(name,position))
