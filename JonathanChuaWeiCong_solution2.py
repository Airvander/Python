# JonathanChuaWeiCong_solution2.py

# Profile Setup
def studentname(myName, myEmail, myBBUsername):
    myName = "Jonathan Chua Wei Cong"
    myEmail = "Jonathancwc@gmail.com"
    myBBUsername = "863fyj6p"
    return myName, myEmail, myBBUsername

# Question 2
def countCharacter(sentence):
    letter_count = 0
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    other_count = 0

    for char in sentence:
        if char.isalpha():
            letter_count += 1
            if char.isupper():
                uppercase_count += 1
            else:
                lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1

    return [letter_count, uppercase_count, lowercase_count, digit_count, other_count]