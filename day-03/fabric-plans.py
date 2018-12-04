from collections import Counter, defaultdict
from functools import reduce
from itertools import groupby
from operator import mul
from pathlib import Path
from typing import DefaultDict, Generator, Set, Tuple


def get_claim(line: str) -> Generator[int, None, None]:
    return (int("".join(g)) for isdigit, g in groupby(line, str.isdigit) if isdigit)


def num_claims_with_overlap(fin: Path) -> int:
    claimed: Counter = Counter()
    with fin.open() as claims:
        for claim in claims:
            _, left, top, width, height = get_claim(claim)
            for x in range(left, left + width):
                for y in range(top, top + height):
                    claimed[x, y] += 1

    return sum(v > 1 for v in claimed.values())


def claim_without_overlap(fin: Path) -> Set[int]:
    claimed: DefaultDict[Tuple[int, int], Set[int]] = defaultdict(set)
    all_ids = set()
    with fin.open() as claims:
        for claim in claims:
            claim_id, left, top, width, height = get_claim(claim)
            all_ids.add(claim_id)
            for x in range(left, left + width):
                for y in range(top, top + height):
                    claimed[x, y].add(claim_id)

    for ids in claimed.values():
        if len(ids) > 1:
            all_ids -= ids

    return all_ids


if __name__ == "__main__":
    fin = Path("input.txt")
    print(num_claims_with_overlap(fin))
    print(*claim_without_overlap(fin))
