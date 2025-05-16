p01 = [['Amber', 'EL4'], ['Bob', 'EL2'], ['Chad', 'EL3'], ['Ben',
'EL4'], ['Charles', 'EL5'], ['Sharon', 'EL6']]
p02 = [['Wesley', 'EL5'], ['Joel', 'EL7'], ['Victor', 'EL3'],
['Bryan', 'EL3'], ['Mabel', 'EL2'], ['Ravi', 'EL2'], ['Pat',
'EL2']]
p03 = [['Pamela', 'EL1'], ['Joseph', 'EL1'], ['Sam', 'EL4'],
['Aaron', 'EL2'], ['Mandy', 'EL5']]

group_list = [p01, p02, p03]
group_name = ['p01', 'p02', 'p03']
modules = ['EL1', 'EL2', 'EL3', 'EL4', 'EL5']
module_total = [0, 0, 0, 0, 0]

i=0

print("Group     Student   Elective")
for group,student,elective in range (len(group_list)) and (len(group_name)) and (len(modules))
group += group_list
student += group_name
elective += modules
print("{:<15},{:<15},{:<15}", .format(group, student, elective))
