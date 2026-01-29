# Assignment 2 FOR Biopython Course done by PARTHIV RAJESH

# Section A

## 1

### A -> Bioinformatics is the field of biotechnology that combines both biology and informatics and is used to access, manage, manipulate different kinds of biological information using computer technologies. This includes DNA, RNA and its types, Genomes, Proteins etc

### B -> Python is used in bioinformatics due to its many libraries that includes different packages that help solve different kinds of data centric problems related to biological information; ex: Biopython – which helps us understand how to manipulate and access biological info regarding RNA, DNA etc


## 2

### A -> Text or a string in python is shown by marking it within double quotations (“”) and a number or integer is shown by just defining it with respect to a variable or another string

### B -> len(sequence) is used to give the length of the entire string or list or array i.e. sequence whereas len(sequence[0]) is used to give the length of the first item of the string/array/list.


## 3

### A -> A
### B -> 5


# Section B

## 4
gene = "ACE2"
gene_dna_seq = "AGTC"

print(gene)
print(gene_dna_seq)

## 5
dna_seq = "ATGCGTACGTA"

print(len(dna_seq))
print(dna_seq[0])
print(dna_seq[10])

# Section C

## 6
dna_sequences = ["ATGC", "CGTAA", "TTAACG"]

print(dna_sequences)
print(len(dna_sequences))

## 7
print(dna_sequences[1])
print(len(dna_sequences[2]))

# Section D

## 8
dna_sequences1 = ["ATGC", "CGTA", "TTAA"]

for d in dna_sequences1:
    print(d)

for dna_sequences1[0] in dna_sequences1:
    print(dna_sequences1[0], len(dna_sequences1[0]))

# Section E

## 1 Storing DNA sequences in a list and using loops is important in bioinformatics instead of creating separate variables is due to efficiency.
## 2 This allows us to manipulate, access various parts of a DNA sequence easily and use it for further research
## 3 In cases of very long DNA sequences, it is not feasible to write separate variables for each sequence as it is not efficient and may cause errors.


