"""
input:
prompt user for dna1
get dna1

process:
dna2 = d1 + d2 + d3  + d4 + d5 + d6

output:
display dna2
"""

base = 'ACGT'
complement = 'TGCA'

dna1 = "ACCGTCG"
dna1 = input("Enter DNA sequence:")

#A=[0] C=[1] C=[2] G=[3] T=[4] C=[5] G=[6]
index = base.find(dna1[0])
dna2 = complement[index]
dna2 = complement[base.find(dna1[1])] + dna2
dna2 = complement[base.find(dna1[2])] + dna2
dna2 = complement[base.find(dna1[3])] + dna2
dna2 = complement[base.find(dna1[4])] + dna2
dna2 = complement[base.find(dna1[5])] + dna2
dna2 = complement[base.find(dna1[6])] + dna2
print(dna2)          
