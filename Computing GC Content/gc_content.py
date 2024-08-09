from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_gc.txt"


for record in SeqIO.parse(file_path, "fasta"):
    print(f"> {record.id}\n{gc_fraction(record)*100:.6f}")



