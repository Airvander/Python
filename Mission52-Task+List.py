#Programming I

#######################
#     Mission 6.1     #
#      Task List      #
#######################

#Background
#==========
#After his success in the driverless vehicle, Tom
#ventures into private investigation services. To keep
#track of his progress on the cases, he like to
#create a task list dynamically according to the
#number of days.
#
#Write a Python program that prompts Tom to enter
#the number of days, and print the day number in
#first column, and spaces for him to fill up his
#task in second column. After every 7 days, there
#should be a heading inserted. 





#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - num



#START CODING FROM HERE
#======================
#Prompt user to enter the number of days
num = 


#Generate task list
def generate_tasklist(num):
    count = 1
    print("Day | Task(s)")
    while count <= num:
            print("{:>2}  |".format(count))
            count += 1
            if count == 7:
                print("Day | Task(s)")
#Do not remove the next line
generate_tasklist(num)





