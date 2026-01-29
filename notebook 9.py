# SeqIO to understand how to use same for GenBank files

from Bio import SeqIO

seq1 = SeqIO.read("COX1_GenBank.gb", "genbank")

print(seq1.id)
print(seq1.description)
print(seq1.annotations)
print(len(seq1))
print(seq1.seq)
print(seq1.features)
print(len(seq1.features))

# Ask python to print me all the features and its location within this genbank file

for features in seq1.features:
    print(features.type, features.location)
## dna has a positive and negative side so when result is coming + side so it starts from the + side of the dna


