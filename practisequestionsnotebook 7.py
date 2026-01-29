from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord



# Practise Questions
# 1

Name = "Parthiv Rajesh"
dna1 = Seq("ATGCGT")
print(dna1)
print()

# 2

Name = "Parthiv Rajesh"
dna2 = Seq("ATGC")
print(dna2.complement())
print(dna2.transcribe())
print()

# 3

Name = "Parthiv Rajesh"
## Bio.seq.seq

# 4

Name = "Parthiv Rajesh"
dna3 = Seq("ATGCAA")
dna3_record = SeqRecord(dna3,
                        "gene1 ",
                        "Sample practise dna3",
                        "sample gene sequence"
                        )

# 5

Name = "Parthiv Rajesh"
dna4 = Seq("ATGC")
dna5 = Seq("TTAA")
dna4_record = SeqRecord(dna4,
                        "geneA",
                        "Sample practise dna4",
                        "sample gene sequence 4")
dna5_record = SeqRecord(dna5,
                        "geneB",
                        "Sample practise dna5",
                        "sample gene sequence 5")

for id in (dna4_record,dna5_record):
    print(id.id)
print()

