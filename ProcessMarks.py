marksList = [89, 77, 55, 69, 50, 60, 11, 10, 14, 20]

#Display Marklist
print("marksList" .format(marksList))
print("The 1st element is {}" .format(marksList[0]))

#Add the two element of marklist and
#assign the result to variable sum
sum = marksList[-1] + marksList[-2]
print('The sum of last 2 elements is {}'.format(sum))

#Double the value in second element of marklist
marksList[1] = marksList[1] * 2
print('Double value of 2nd element is {}'.format(marksList[1]))

