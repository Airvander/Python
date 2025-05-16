#Programming I

#######################
#     Mission 6.1     #
#     Morse Code      #
#######################

#Background
#==========
#Tom has a partner to help him with the cases. To
#communicate to each other, they uses Morse code.
#Write a Python program that prompts the user to
#key in a number, convert each digit according to
#the diagram below. Each Morse code of a digit has
#to be separated with 3 spaces. The following shows
#a sample output of the program.
#
#Enter a number to convert:9
#The morse code for 9 is ----.
#>>> 
#Enter a number to convert:101
#The morse code for 101 is .----   -----   .----
#>>> 


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - num
#   - morse_code



#START CODING FROM HERE
#======================

#Prompt user to enter the number to convert
num = input('Enter a number to convert:')


#convert to morse code
def convert_code(num):
    morse_code = []
    for i in range(len(num)):
        if num[int(i)] == '1':
            code = '.----'
        elif num[int(i)] == '2':
            code = '..---'
        elif num[int(i)] == '3':
            code = '...--'
        elif num[int(i)] == '4':
            code = '....-'
        elif num[int(i)] == '5':
            code = '.....'
        elif num[int(i)] == '6':
            code = '-....'
        elif num[int(i)] == '7':
            code = '--...'
        elif num[int(i)] == '8':
            code = '---..'
        elif num[int(i)] == '9':
            code = '----.'
        elif num[int(i)] == '0':
            code = '-----'
        morse_code.append(code)
    morse_code = '   '.join(morse_code)
    print(morse_code)
    return morse_code#Do not remove this line
#Do not remove the next line
convert_code(num)

    
#Do not remove the next line
convert_code(num)

#test cases
#input 9        output ----.
#input 101      output .----   -----   .----
#input 0906     output -----   ----.   -----   -....

