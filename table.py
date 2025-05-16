num = int(input('please enter a number: '))
table = 1

while table <= 10 :
    total = num * table
    
    print('{} x {} = {}'.format (num,table,total))
    table = table + 1
