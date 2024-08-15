from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq

file_path = Path(__file__).parent / "rosalind_splc.txt"



records = list(SeqIO.parse(file_path, "fasta"))
dna_string = records[0].seq
introns = records[1:]

for record in introns:
    dna_string = dna_string.replace(record.seq, "")

print(Seq(dna_string).translate().replace("*", ""))


