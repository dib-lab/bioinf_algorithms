#! /usr/bin/env python

import random

from ba2c import profile_most_probable
from ba2d import score
from ba2e import profile_matrix


def randomized_motif_search(dna, k, t):
    motifs = []
    for seq in dna:
        rand_pos = random.randint(0, len(seq) - k)
        motifs.append(seq[rand_pos : rand_pos + k])

    best = motifs
    score_best = score(best)

    while True:
        profile = profile_matrix(motifs, k)
        motifs = [profile_most_probable(seq, k, profile) for seq in dna]

        score_motifs = score(motifs)
        if score_motifs < score_best:
            best = motifs
            score_best = score_motifs
        else:
            return best, score_best


def repeated_randomized_motif_search(dna, k, t, *, times=1000):
    best, score_best = randomized_motif_search(dna, k, t)
    for _ in range(times - 1):
        new_best, new_score = randomized_motif_search(dna, k, t)
        if new_score < score_best:
            best = new_best
            score_best = new_score

    return best


result = repeated_randomized_motif_search(
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA".split(),
    8,
    5,
)
assert (
    score(result) <= score("TCTCGGGG CCAAGGTG TACAGGCG TTCAGGTG TCCACGTG".split()) + 1
), result


if __name__ == "__main__":
    with open("data/rosalind_ba2f.txt", "r") as dataset:
        k, t = [int(d) for d in dataset.readline().rstrip().split()]
        text = [l.rstrip() for l in dataset.readlines()]
    print(*repeated_randomized_motif_search(text, k, t), sep="\n")
