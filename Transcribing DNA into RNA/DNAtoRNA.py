from Bio.Seq import Seq
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_rna.txt"
data = file_path.read_text()
seq_data = Seq(data)

def dna_to_rna(s):
    """Convert DNA to RNA"""
    return Seq.transcribe(s)

print(dna_to_rna(seq_data))