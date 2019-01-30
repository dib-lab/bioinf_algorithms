#! /usr/bin/env python

from collections import defaultdict


def find_clumps(Genome, ksize, clump_length, times):
    # define kmers greater than times
    keepers = set()

    # define dictionary of kmers
    kmer_counts = defaultdict(int)

    # For the first clump we need to count all kmers
    for kmer_index in range(clump_length - ksize + 1):
        kmer = Genome[kmer_index : kmer_index + ksize]
        kmer_counts[kmer] += 1

        if kmer_counts[kmer] >= times:
            keepers.add(kmer)

    # for all the subsequent clumps we need to
    # - decrease the count for the first kmer from the previous clump
    # - add the last kmer from the current clump
    # (why? all the other kmers are shared between current and previous clumps!)
    for clump_index in range(1, len(Genome) - clump_length + 1):
        # decrease count from first kmer from previous clump
        prev_first_kmer = Genome[clump_index - 1 : clump_index + ksize - 1]
        kmer_counts[prev_first_kmer] -= 1

        # add the last kmer from current clump
        last_kmer_start = clump_index + clump_length - ksize
        kmer = Genome[last_kmer_start : last_kmer_start + ksize]
        kmer_counts[kmer] += 1

        if kmer_counts[kmer] >= times:
            keepers.add(kmer)

    return keepers


assert find_clumps(
    "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC",
    5,
    75,
    4,
) == set("CGACA GAAGA AATGT".split())


if __name__ == "__main__":
    with open("data/rosalind_ba1e.txt", "r") as dataset:
        genome = dataset.readline().rstrip()
        k, L, t = [int(i) for i in dataset.readline().rstrip().split()]
    print(*find_clumps(genome, k, L, t), sep=" ")
