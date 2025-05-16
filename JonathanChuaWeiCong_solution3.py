# JonathanChuaWeiCong_solution3.py

# Profile Setup
def studentname(myName, myEmail, myBBUsername):
    myName = "Jonathan Chua Wei Cong"
    myEmail = "Jonathancwc@gmail.com"
    myBBUsername = "863fyj6p"
    return myName, myEmail, myBBUsername

# Question 3
def excludeItem(item1, item2):
    result = list(set(item1) & set(item2))
    return result