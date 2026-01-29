# Uniprot is a database that stores protein sequences along with detailed information about them, stores annotated proteins, not just raw sequences

from Bio import SeqIO

# read is for single and # parse is for multiple files within it
seq = SeqIO.read("uniprot_insulin.fasta", "fasta")

print("Parthiv Rajesh")
print(seq.id)
print(seq.name)
print(seq.description)
print(len(seq))
print(seq.seq)
print("-"*45)

from Bio import SeqIO

record = SeqIO.parse("uniprot_combined_proteins.fasta", "fasta")

for r in record:
    print(r.id)
    print(r.name)
    print(r.description)
    print(len(r))
    print(r.seq)
    print()



