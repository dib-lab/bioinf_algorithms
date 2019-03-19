#! /usr/bin/env python

from collections import defaultdict
from functools import lru_cache
from itertools import product

from ba1g import hamming


@lru_cache(2048)
def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}

    neighborhood = set()
    for text in neighbors(pattern[1:], d):
        if hamming(pattern[1:], text) < d:
            for bp in "ACGT":
                neighborhood.add(bp + text)
        else:
            neighborhood.add(pattern[0] + text)

    return neighborhood


def frequent_words_with_mismatches_all(text, k, distance):
    frequent_patterns = set()
    kmers = defaultdict(int)
    max_freq = 0

    for kmer in product("ACGT", repeat=k):
        pattern = "".join(kmer)
        for i in range(len(text) - k):
            if hamming(text[i : i + k], pattern) <= distance:
                kmers[pattern] += 1
                current_freq = kmers[pattern]
                if current_freq == max_freq:
                    frequent_patterns.add(pattern)
                elif current_freq > max_freq:
                    frequent_patterns = set([pattern])
                    max_freq = current_freq

    return frequent_patterns


def frequent_words_with_mismatches(text, k, distance):
    frequent_patterns = set()
    kmers = defaultdict(int)
    max_freq = 0

    for i in range(len(text) - k):
        for pattern in neighbors(text[i : i + k], distance):
            kmers[pattern] += 1

            current_freq = kmers[pattern]
            if current_freq == max_freq:
                frequent_patterns.add(pattern)
            elif current_freq > max_freq:
                frequent_patterns = {pattern}
                max_freq = current_freq

    return frequent_patterns


assert frequent_words_with_mismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1) == set(
    "GATG ATGC ATGT".split()
)


if __name__ == "__main__":
    with open("data/rosalind_ba1i.txt", "r") as dataset:
        text = dataset.readline().rstrip()
        k, d = [int(i) for i in dataset.readline().rstrip().split()]
    print(*frequent_words_with_mismatches(text, k, d))
