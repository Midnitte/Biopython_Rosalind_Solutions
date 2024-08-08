from Bio.Seq import Seq
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_revc.txt"
data = file_path.read_text()
seq_data = Seq(data)

def reverse_comp(s):
    """Return the reverse complement of s"""
    return Seq.reverse_complement(s)

print(reverse_comp(seq_data))