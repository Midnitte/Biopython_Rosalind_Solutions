from Bio.Seq import Seq
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_prot.txt"
data = file_path.read_text()
seq_data = Seq(data)


def mut_count(s):
    """Return the protein encoded by RNA."""
    return s.translate()

print(str(mut_count(seq_data))[:-1])