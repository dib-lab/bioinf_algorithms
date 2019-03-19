#! /usr/bin/env python

from itertools import product
import sys

from ba1g import hamming


def dist(pattern, text):
    distances = []
    k = len(pattern)
    for dna in text:
        current_min = sys.maxsize
        for i in range(len(dna) - k + 1):
            current_min = min(hamming(pattern, dna[i : i + k]), current_min)
        distances.append(current_min)

    return sum(distances)


def median_string(text, k):
    distance = sys.maxsize
    for pattern in product("ACGT", repeat=k):
        pattern = "".join(pattern)
        d = dist(pattern, text)
        if d < distance:
            distance = d
            median = pattern
    return median


assert median_string(
    "AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG".split(), 3
) in ("GAC", "ACG")


if __name__ == "__main__":
    with open("data/rosalind_ba2b.txt", "r") as dataset:
        k = int(dataset.readline().rstrip())
        text = [s.rstrip() for s in dataset.readlines()]
    print(median_string(text, k))
