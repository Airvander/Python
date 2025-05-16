def calculateCharge(pages):
    if (pages <=100):
        charge = 0.03 * pages
    elif(pages <= 300):
        charge = (0.03 * 100) + (pages-100)*0.02
    else:
        charge = (0.03 *100) + (0.02 * 200) + (pages-300) *0.01

    return charge

for pages in range(0,501,50):
    charge = calculateCharge(pages)
    gst = calculateGST(Charge)
    
