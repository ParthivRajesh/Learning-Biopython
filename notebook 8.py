# SeqIO or Sequence Input and Output to understand the fasta file which we download from NCBI or similar sites

from Bio import SeqIO

seq1 = SeqIO.read("COX1.fasta", "fasta")

print(seq1.id)
print(seq1.description)
print(len(seq1))
print(seq1.seq)
print()

seq2 = SeqIO.read("Insulin_INS.fasta", "fasta")

print(seq2.id)
print(seq2.description)
print(len(seq2))
print(seq2.seq)
print()

