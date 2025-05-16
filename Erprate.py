card_value = float(input('enter card value:'))
time_of_entry = float(input('enter time of entry:'))

if time_of_entry < 12.00:
    erp_rate = 0
elif time_of_entry >= 12.00 and time_of_entry < 17.30:
    erp_rate = 0.50
elif time_of_entry >= 17.30 and time_of_entry < 17.35:
    erp_rate = 1.00
elif time_of_entry >= 17.35 and time_of_entry < 18.00:
    erp_rate = 1.50
elif  time_of_entry >= 18.00 and time_of_entry < 18.55:
    erp_rate = 2.00
elif  time_of_entry >= 18.55 and time_of_entry < 19.00:
    erp_rate = 1.50
elif time_of_entry >= 19.00 and time_of_entry < 19.55:
    erp_rate = 1.00
elif  time_of_entry >= 19.55 and time_of_entry < 20.00:
    erp_rate = 0.50
elif time_of_entry >= 20.00:
    erp_rate = 0

print('your erp rate is:', "{:.2f}".format(erp_rate))
if (card_value - erp_rate) >= 0: 
    card_value = card_value - erp_rate
    successful_deduction = True

    print('new value in cash card:',"{:.2f},".format(card_value),successful_deduction)

else:
    successful_deduction = False
    print('insufficent amount in cash card' ,"{:.2f},".format(card_value),successful_deduction)
