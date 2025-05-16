#prompt tom to enter how much coins he have
cent50 = (input("How many 50 cent coins do you have with you? : ")) 
cent20 = (input("How many 20 cent coins do you have with you? : "))
cent10 = (input("How many 10 cent coins do you have with you? : "))
cent5 = (input("How many 5 cent coins do you have with you? : "))

cent50 = float(cent50)
cent20 = float(cent20)
cent10 = float(cent10)
cent5 = float(cent5)

#calculate total amount of coins
total = (cent50 * 0.5) + (cent20 * 0.2) + (cent10 * 0.1) + (cent5 * 0.05)

#display total amount
print("Your grand total is $" +'{:0.1f}'.format(total)) 
