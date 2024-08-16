from pathlib import Path
from functools import lru_cache

file_path = Path(__file__).parent / "rosalind_fib.txt"

n, k = file_path.read_text().split(" ")
n, k = int(n), int(k)

@lru_cache(None)
def fib_seq(num: int, litter: int) -> int:
    if num < 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_seq(num - 1, litter) + fib_seq(num - 2, litter)*litter

print(fib_seq(n, k))