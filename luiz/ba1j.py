#! /usr/bin/env python

from collections import defaultdict

from ba1c import revc
from ba1i import neighbors


def frequent_words_with_mismatches_and_rc(text, k, distance):
    frequent_patterns = set()
    kmers = defaultdict(int)
    max_freq = 0

    for i in range(len(text) - k):
        for pattern in neighbors(text[i : i + k], distance):
            kmers[pattern] += 1
            rc = revc(pattern)

            current_freq = kmers[pattern] + kmers[rc]
            if current_freq == max_freq:
                frequent_patterns.add(pattern)
                frequent_patterns.add(rc)
            elif current_freq > max_freq:
                frequent_patterns = set([pattern, rc])
                max_freq = current_freq

    return frequent_patterns


assert frequent_words_with_mismatches_and_rc(
    "ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1
) == set("ATGT ACAT".split())


if __name__ == "__main__":
    with open("data/rosalind_ba1j.txt", "r") as dataset:
        text = dataset.readline().rstrip()
        k, d = [int(i) for i in dataset.readline().rstrip().split()]
    print(*frequent_words_with_mismatches_and_rc(text, k, d))
