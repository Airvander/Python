page = int(input("enter number of pages to print: "))

if page <= 100:
    total = 0.03 * page
   
elif page <= 300:
    total = (0.03 * 100) + (0.02 * (page - 100))
        
else:
    total = (0.03 * 100) + (0.02 * 200) + (0.01 * (page - 300))
print("cost of printing {:d} page is ${:.2f}".format(page,total))
  
