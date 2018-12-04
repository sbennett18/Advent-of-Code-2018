from collections import Counter
from functools import reduce
from operator import mul
from pathlib import Path
from typing import Dict, Optional


def has_repeated_letters(letters: Counter, num_repeated: int) -> bool:
    for v in letters.values():
        if v == num_repeated:
            return True
    return False


def checksum(fin: Path) -> int:
    repeats: Counter = Counter()
    with fin.open() as box_ids:
        for id in box_ids:
            id = id.strip()
            letters: Counter = Counter()
            for l in id:
                letters[l] += 1

            for x in (2, 3):
                if has_repeated_letters(letters, x):
                    repeats[x] += 1

    return reduce(mul, repeats.values(), 1)


def common_box_ids(fin: Path) -> Optional[str]:
    hasher: set = set()
    with fin.open() as box_ids:
        for id in box_ids:
            id = id.strip()
            for i, _ in enumerate(id):
                key = (id[:i], id[i + 1 :])
                # print(id, "\t", key)
                if key in hasher:
                    return "".join(key)
                hasher.add(key)
    return None


if __name__ == "__main__":
    fin = Path("input.txt")
    print(checksum(fin))
    print(common_box_ids(fin))
