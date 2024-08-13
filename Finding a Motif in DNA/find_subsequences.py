from pathlib import Path
import regex as re

file_path = Path(__file__).parent / "rosalind_subs.txt"

string, substring, _ = file_path.read_text().split("\n")
result = ""

for match in re.finditer(substring, string, overlapped=True):
    result += str(match.start()+1) + " "
print(result)