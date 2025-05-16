def obtian_grade(mark):
    if (mark <0 or mark > 100):
        return"Invaid"
    elif (mark >= 84.5):
        return 'A+'
    elif (mark >= 74.5):
        return'A'
    elif (mark >= 69.5):
        return 'B+'
    elif (mark >= 64.5):
        return 'B'
    elif (mark >= 59.5):
        return 'C+'
    elif (mark >= 54.5):
        return 'C'
    elif (mark >= 49.5):
        return 'D'

mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]
