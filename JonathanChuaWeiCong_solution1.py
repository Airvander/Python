# JonathanChuaWeiCong_solution1.py

# Profile Setup
def studentname(myName, myEmail, myBBUsername):
    myName = "Jonathan Chua Wei Cong"
    myEmail = "Jonathancwc@gmail.com"
    myBBUsername = "863fyj6p"
    return myName, myEmail, myBBUsername

# Question 1
def calAverage(num_list):
    if not num_list:
        return 0.00

    total = sum(num_list)
    result = total / len(num_list)

    return round(result, 2)