# Epidermal Keratin Protein - Biopython Course Project - Parthiv Rajesh@https://github.com/ParthivRajesh/Parthiv
# Reference Link - https://www.ncbi.nlm.nih.gov/nuccore/J00124.1?report=fasta

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import Counter
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

print("SECTION A")
print("-"*50)
print()
protein = SeqIO.read("EpidermalKeratin.fasta", "fasta")
# Printing the Seq ID
print(protein.id)
print()

# Printing the Seq Length
print(len(protein))
print()

# Printing the Amino acid composition
aa_counts = Counter(str(protein.seq))
print("The amino acid composition: ", aa_counts)
print()

print("SECTION B")
print("-"*50)
print()
# Determining whether Sequence is of low quality or not
## the pHred quality score helps us determine whether a sequence is of low quality or not, this is measured by <20 for low quality

protein1 = SeqIO.read("EpidermalKeratin.fasta", "fasta")

if len(protein) < 20:
    print("Sequence is of lower threshold quality.")
else:
    print("Sequence is of an acceptable threshold quality.")
print()

## Removing Ambiguous Sequences
if "N" in protein.seq:
    print("Sequence contains ambiguous sequences.")
print()

print("SECTION C")
print("-"*50)
print()
# Translating sequence to protein

## Extracting only fasta file
nucleotide_Seq = protein1.seq

## Trim the length to nearest multiple of 3 to fix partial codons error
trimmed_length_seq = len(nucleotide_Seq) - (len(nucleotide_Seq) % 3)
nucleotide_Seq_trimmed = nucleotide_Seq[:trimmed_length_seq]

## Translating Sequence
protein = nucleotide_Seq_trimmed.translate()
print("Original Sequence: ", nucleotide_Seq)
print("Trimmed Sequence: ", nucleotide_Seq_trimmed)
print("Protein Sequence: ", protein)
print()

print("SECTION D")
print("-"*50)
print()
# Perform Similarity Search using BLAST

# Generating a BLAST XML File for Similarity Search
pblast_protein = NCBIWWW.qblast(
    program = "blastp", #As we have a nucleotide FASTA file so we run nucleotide blast
    database = "nr",
    sequence = str(protein)
)

with open("nblast_result_protein.xml","w") as p:
    p.write(pblast_protein.read())
print("The nblast result is done! ")
print()

# Running HSP alignments for Similarity Search

with open("nblast_result_protein.xml","r") as p:
    protein_nblast_record = NCBIXML.read(p)

for alignment in protein_nblast_record.alignments[:5]:
    for hsp in alignment.hsps:
        print("Sequence: ", alignment.hit_def)
        print("Length:", alignment.length)
        print("Identity:", hsp.identities)
        print("Alignment length:", hsp.align_length)
        print("E-value:", hsp.expect)
        print()

# Identify: Closest Homologs, Conserved Regions, Evolutionary Hints

## Closest Homologs
for alignment in protein_nblast_record.alignments[:5]:  # top 5 hits
    for hsp in alignment.hsps:
        print("Sequence:", alignment.hit_def)
        print("Length:", alignment.length)
        print("Identity:", hsp.identities)
        print("Alignment length:", hsp.align_length)
        print("E-value:", hsp.expect)
        print()

## Conserved Regions
for alignment in protein_nblast_record.alignments[:3]:
    for hsp in alignment.hsps:
        if hsp.identities / hsp.align_length > 0.7:
            print("Conserved regions found are: ")
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
            print()

## Evolutionary Hints
species_hits = []

for alignment in protein_nblast_record.alignments[:10]:
    species_hits.append(alignment.hit_def)

print("Species distribution:")
for hit in species_hits:
    print(hit)
print()

print("SECTION E")
print("-"*50)
print()
# Functional Annotation

## Getting Annotations through ExPASy and SwissProt
from Bio import ExPASy
from Bio import SwissProt

accession = "P02533"
handle = ExPASy.get_sprot_raw(accession)
record = SwissProt.read(handle)

## Biological Role
print("Function of Protein: ", record.description)
print()

## Organism Relevance
print("Biological Role of Protein: ", record.organism)
print()

## Function
for c in record.comments:
    if c.startswith("FUNCTION"):
        print(c)
print()

# Questions
## What does this sequence likely do? - This sequence is responsible for proteins that are differently expressed in different tissues and a different stages of differentiation and development in Homo sapiens.
## Why do they think so? - This sequence has a main function: The nonhelical tail domain is involved in promoting KRT5- KRT14 filaments to self-organize into large bundles and enhances the mechanical properties involved in resilience of keratin intermediate filaments in vitro.
## What evidence supports their claim? - This sequence is directly taken from NCBI with reference link provided on top

# Done by Parthiv Rajesh