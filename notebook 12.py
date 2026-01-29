from Bio.Blast import NCBIXML

with open("blast_result.xml", "w") as b:
    blast_record = NCBIXML.read(b)

print(len(blast_record.alignments))

first_alignment = blast_record.alignments[0]
print(first_alignment.title)
print(first_alignment.length)

# for a in blast_record.alignments:
#     print(a.title)

print(len(first_alignment.hsps)) # HSPs or high scoring segment pairs or hsp is the exact region where the sequences match

first_hsp = first_alignment.hsps[0]
print(first_hsp.score) # the alignment strength or how good the alignment is
print(first_hsp.expect) # the e value tells us how reliable the alignment is

# ALL these 3 represent one query sequence
print("Query Sequence: ")
print(first_hsp.query)

print("Matched Sequence: ")
print(first_hsp.sbjct)

print("Alignment Sequence: ")
print(first_hsp.match)

print("Query range: ", first_hsp.query_start, "-", first_hsp.query_end)
print("Subject range: ", first_hsp.sbjct_start, "-",first_hsp.sbjct_end)

