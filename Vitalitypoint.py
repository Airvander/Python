distance = int(input("enter distance walking or running in km:",))

if distance < 25:
    value = 2
    print('You have receive $' + "{}".format(value), 'Popular eVocher')
elif distance >= 25 and distance < 50:
    value = 5
    print('You have receive $' + "{}".format(value), 'Cold Storage eVocher')    
elif distance >= 50 and distance < 75:
    value = 10
    print('You have receive $' + "{}".format(value), 'Starbucks eVocher')
elif distance >75:
    value = 20
    print('You have receive $' + "{}".format(value), 'Subway eVocher')
