from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_gc.txt"

result = None
highest_gc = 0.00001

for record in SeqIO.parse(file_path, "fasta"):
    if float(gc_fraction(record)*100.0) > float(highest_gc):
        highest_gc = gc_fraction(record)*100.000000
        result = f"{record.id}\n{gc_fraction(record)*100:.6f}"
print(result)



