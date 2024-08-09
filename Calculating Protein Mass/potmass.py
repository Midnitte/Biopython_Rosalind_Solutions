from Bio.SeqUtils.ProtParam import ProteinAnalysis
from pathlib import Path

file_path = Path(__file__).parent / "rosalind_prtm.txt"
data = file_path.read_text()
seq_data = ProteinAnalysis(data, monoisotopic=True)


def prot_mass(s):
    """Return the protein mass."""
    # Subtract weight of one water molecule
    return round(s.molecular_weight() - 18.010565, 3)


print(prot_mass(seq_data))
