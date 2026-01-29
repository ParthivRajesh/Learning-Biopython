from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dna = Seq("ATGCGT")
record = SeqRecord(dna,
                   id = "gene1",
                   name = "example gene",
                   description = "sample dna sequence record"
                   )

print(record.id)
print(record.name)
print(record.description)
print(record.seq)

print()

protein_seq = Seq("MKTLLV")
protein_record = SeqRecord(protein_seq,
                           "protein 1",
                           "example protein",
                           "sample protein record"
                           )

print(protein_record.id)
print(protein_record.name)
print(protein_record.description)
print(protein_record.seq)

print()





