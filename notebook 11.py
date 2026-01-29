# BLAST stands for Basic Local Alignment Search Tool
# Blastp is for proteins
# Blastn is for nucleotides

from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("uniprot_insulin.fasta", "fasta")

blastp_protein = NCBIWWW.qblast(
    program = "blastp",
    database = "nr", # non reductant protein database contains protein sequences form many organisms and removes duplicate sequences to give us a better quality result
    sequence = record.seq # or you can manually paste the sequence - although obviously this is more efficient
)
# print(blastp_protein)

with open ("blast_result.xml", "w") as b:
    # we are going to open a file called blast_result.xml and open it in write mode, and then we open this "blast_result.xml" as b so like it's a nickname
    b.write(blastp_protein.read())

print("The blast result for xml is done!")

