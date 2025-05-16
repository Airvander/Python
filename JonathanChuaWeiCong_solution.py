# JonathanChuaWeiCong_solution.py

# Profile Setup
def studentname(myName, myEmail, myBBUsername):
    myName = "Jonathan Chua Wei Cong"
    myEmail = "683fyj6p@psba.edu.sg"
    myBBUsername = "863fyj6p"
    return myName, myEmail, myBBUsername

# Question 1
def calAverage(num_list):
    if not num_list:
        return 0.00

    total = sum(num_list)
    avg = total / len(num_list)

    return round(avg, 2)

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

# Question 3
def excludeItem(item1, item2):
    result = list(set(item1) & set(item2))
    return result

# Question 4
def secondLarge(num_list):
    if not all(isinstance(x, int) for x in num_list):
        return -999  # Return -999 if the list contains non-integer elements

    unique_nums = list(set(num_list))  # Remove duplicates from the list
    unique_nums.sort()  # Sort the list in ascending order

    if len(unique_nums) == 1:
        return unique_nums[0]  # Return the only number if there's only one in the list
    elif len(unique_nums) == 2:
        return min(unique_nums)  # Return the smallest number if there are only two in the list
    else:
        return unique_nums[-2]  # Return the second largest number

# Question 5

def isValidPassword(password):
    # Criteria 1: Must have a combination of uppercase and lowercase letters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if not (has_upper and has_lower):
        return False

    # Criteria 2: Must have at least 3 digits
    digit_count = sum(char.isdigit() for char in password)
    if digit_count < 3:
        return False

    # Criteria 3: Must have at least 2 special characters (including whitespace)
    special_chars = "!@#$%^&*()_-+=[]{};:'\"\\|,.<>/?`~ "
    special_count = sum(char in special_chars for char in password)
    if special_count < 2:
        return False

    # Criteria 4: Must have at least 10 characters (combination of alphanumeric and special symbols)
    if len(password) < 10:
        return False

    return True
