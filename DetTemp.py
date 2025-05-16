temp = int(input('please enter outdoor temperature :'))

if temp <= -5:
    print('go bowling')
elif temp <= 0:
    print('go skiing')
elif temp <= 20:
    print('go jogging')
elif temp <= 25:
    print('play tennis')
    print('wear white clothes')
elif temp <= 30:
    print('go sun-tanning in the park')
else:
    print('go swimming')
