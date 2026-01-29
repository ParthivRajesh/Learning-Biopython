# import Bio
# print(Bio.__version__)

from Bio.Seq import Seq # Bio is the biopython package, .Seq is the module of Biopython package and Seq is the class of that module that we are importing

dna = Seq("ATGCGTTAC")
print(dna)
print(dna.complement()) # Printing the complement sequence to given sequence

rna = dna.transcribe() # Transcription of dna to rna - i mean it only works on rna
print(rna)

protein = rna.translate() # Translation of rna to protein
print(protein)

protein1 = dna.translate() # Translation of dna to protein (shortcut)
print(protein1)





