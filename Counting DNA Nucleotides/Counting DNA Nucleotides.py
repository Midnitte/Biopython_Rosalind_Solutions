from Bio.Seq import Seq
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_dna.txt"
data = file_path.read_text()
seq_data = Seq(data)


def nucleotide_count():
    """Return a count of each nucleotide as a string."""
    return f"{seq_data.count("A")} {seq_data.count("C")} {seq_data.count("G")} {seq_data.count("T")}"


print(nucleotide_count())
