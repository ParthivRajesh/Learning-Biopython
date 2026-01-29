from pyexpat import features

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Practise Questions by Parthiv Rajesh

# Section A
print("Section A")
print()
## Task 1
dna = Seq("ATGCCAT")
dna_record = SeqRecord(dna,
                       id = "Sample_record_gene",
                       name = "Sample_gene",
                       description = "Sample record"
                       )

print(dna_record.id)
print(dna_record.name)
print(dna_record.description)
print()

## Task 2
dna_record.description = "Sample gene record"
print(dna_record.description)
print()

## Task 3
print(type(dna_record)) # what this does is that it tells us that dna_record is an object of the seqrecord class
print(type(dna_record.seq)) # what this means is that dna_record.seq is an object of the seq class
print("-"*40)

# Section B
print("Section B")
print()
## Task 4

dna1 = SeqIO.read("single_gene.fasta", "fasta")
print(dna1.id)
print(dna1.description)
print(len(dna1))
print()

## Task 5

print(dna1.id)
print(dna1.name)
print(dna1.description)
print()

# the id and name looks the same because in fasta files it is not defined to give different tags to name and id
# this is why biopython prints the id and name same for those separate functions

## Task 6

print(dna1.seq[:5])
print(dna1.seq[-5:])
print("-"*40)


# Section C
print("Section C")
print()
## Task 7


dna2 = SeqIO.parse("multi_genes.fasta","fasta")

for seq in dna2:
    print(seq.id)
    print(len(seq))
    print()

## Task 8

count = 0
for c in SeqIO.parse("multi_genes.fasta", "fasta"):
    count += 1

print("Count of genes present are:", count)
print()

## Task 9

# dna2 = SeqIO.parse("multi_genes.fasta", "fasta")
#
# length_seq = sequence[0]
#
# for s in dna2:
#     if len(s.seq) > len(length_seq.seq):
#         length_seq = sequence
#     print("The id of the longest sequence: ", length_seq.id)
#     print("The length of the longest sequence: ", len(length_seq))
print("-"*40)


# Section D
print("Section D")
print()
## Task 10

dna3 = SeqIO.read("gene_record.gb","genbank")
print(dna3.id)
print(dna3.description)
print(dna3.features)
print()

## Task 11

for feature in dna3.features:
    print(feature.type)
print()

## Task 12

print(dna3.features)

for cds in dna3.features:
    # noinspection PyUnboundLocalVariable
    if feature.type == "CDS":
        print(feature.location)
        print(feature.location.strand)
        print()
# Positive DNA Strand and location from 0th base pair until 1542 base pairs



