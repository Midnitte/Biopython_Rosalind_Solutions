from Bio.Seq import Seq
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_hamm.txt"
data = file_path.read_text()

seq1, seq2 = [Seq(a) for a in data.splitlines()]

def mut_count(s, t):
    """Return the mutation count of two sequences."""
    return sum(1 for a, b in zip(s, t) if a != b)

print(mut_count(seq1, seq2))