secs = int(input("Enter time to be converted (in sec):"))
hrs = secs // 3600
secs = secs % 3600
mins = secs // 60
secs = secs % 60
print("Time :", hrs, "hr,", mins, "min,", secs, "sec")
