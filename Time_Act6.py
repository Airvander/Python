secs = int(input("Enter time to be converted (in secs): "))
hrs = secs // 3600 # (//) secs to hrs 3600sec = 1hr
secs = secs % 3600 # (%) reminder i.e 3602 2secs
mins = secs // 60 # (//) sec to min
secs = secs % 60 # (%) reminder i.e 62 = 2secs

print("Time :", hrs, "hr," , mins, "min, ", secs, "sec") 
