import math
sidea=int(intput('enter length of side A:', sidea))
sideb=int(intput('enter length of side B:', sideb))
sidec=int(intput('enter length of side C:', sidec))



if (sidea + sideb) > sidec and (sideb + sidec) > sidea and (sidec + sidea) > sideb:
    s = a+b+c/2
    area = math.sqrt(s*(s-sidea)*(s-sideb)*(s-sidec))
    print("Input length can form a triangle of area {:.02d}"math.sqrt(area))
else 
    print("Input length cannot form a triangle of ")
