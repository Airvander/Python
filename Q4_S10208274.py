binary = input('Enter an 8-bit binary number: ')
decimal = (binary[0] * 2**7) + (binary[1] * 2**6) + (binary[2] * 2**5) + (binary[3] * 2**4) + (binary[4] * 2**3) + (binary[5] * 2**2) + (binary[6] * 2**1) + (binary[7]) * 2**0
print(decimal)

i = 0
index = 0

for i =< 7:
    decimal = binary[0] * 2**7
    i += 1
    
