# Practise Questions (Lesson 7) - Parthiv Rajesh
# Section A

## 1
# Biopython is a package downloadable within python that can be used to store, access, manipulate and extract biological information like DNA, RNA etc
## 2
# Python does not come with the packages and tools that will logically process biological information into insights, biopython introduces such tools and modules to help us solve those issues.
## 3
# transcribing dna to rna using dna.transcribe function and translation of rna to protein using dna.translate function
## 4
# .Seq module

# Section B

## 5
# pip install biopython
## 6
# from Bio.Seq import Seq

# Section C

## 7
from Bio.Seq import Seq

dna = Seq("ATGCAA")
print(dna)

# Section D

## 8
dna_seq = Seq("ATGCGT")
print(dna_seq.complement())
print(dna_seq.transcribe())
print(dna_seq.translate())

# Section E

## 9
# TACG

# Section F

## 10
# Python essentially does not contain the required logic to process, manipulate, access and extract biological information like DNA, RNA or proteins.
# Biopython helps to solve do this by incorporating logic to such biological-info based questions to understand them and get meaningful insights


