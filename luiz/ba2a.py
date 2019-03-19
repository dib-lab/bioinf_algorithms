#! /usr/bin/env python

from ba1g import hamming
from ba1i import neighbors


def motif_enumeration(text, k, distance):
    patterns = set()

    first = text[0]
    for i in range(len(first) - k + 1):
        pattern = first[i : i + k]
        for pattern_p in neighbors(pattern, distance):
            patterns.add(pattern_p)

    for dna in text[1:]:
        current_patterns = set()

        for i in range(len(dna) - k + 1):
            for pattern_p in patterns:
                if hamming(dna[i : i + k], pattern_p) <= distance:
                    current_patterns.add(pattern_p)

        patterns = current_patterns

    return patterns


assert motif_enumeration("ATTTGGC TGCCTTA CGGTATC GAAAATT".split(), 3, 1) == set(
    "ATA ATT GTT TTT".split()
)


if __name__ == "__main__":
    with open("data/rosalind_ba2a.txt", "r") as dataset:
        k, d = [int(i) for i in dataset.readline().rstrip().split()]
        text = [s.rstrip() for s in dataset.readlines()]
    print(*motif_enumeration(text, k, d))
