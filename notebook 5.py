# Introduction

seq = ["ATGC", "GGCTA", "TTAAC"]
print(type(seq))

print(seq[2])
print(len(seq))
print(len(seq[1]))

# For loops

for s in seq:
    print(s)

genes = ["BRCA1", "TP53", "ACE2"]

for g in genes:
    print(g)

fruit = ["apple" , "banana", "mango"]

for f in fruit:
    print(f)


# Practise Questions

# 1 - Done Orally

# 2
name = "Parthiv Rajesh"
dna_sequences = ["ATGC","CGTAA","TTGCA"]

print(dna_sequences)
print(type(dna_sequences))

for d in dna_sequences:
    print(d)

# 3
name = "Parthiv Rajesh"

print(len(dna_sequences))
print(len(dna_sequences[0]))

# 4
name = "Parthiv Rajesh"

dna_sequences1 = ["ATGCG", "GGCTA", "TTAAC"]

print(dna_sequences1[1][0])
print(dna_sequences1[2][4])

# 5
name = "Parthiv Rajesh"

dna_sequences3 = ["ATGC", "CGTA", "TTAA"]

for d in dna_sequences3:
    print(d)

# 6 -> Optional for # 4-Understanding
name = "Parthiv Rajesh"

dna_sequences2 = ["GGTCA", "ATGGCT", "AATTGG"]

## Print the 4th nucleotide of 3rd dna sequence
print(dna_sequences2[2][3])

## print the last nucleotide of 1st dna sequence
print(dna_sequences2[0][4])





