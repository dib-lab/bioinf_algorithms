#! /usr/bin/env python

import random

from ba2c import profile_most_probable
from ba2d import score
from ba2e import profile_matrix


def gibbs_sampler(dna, k, t, N):
    motifs = []
    for seq in dna:
        rand_pos = random.randint(0, len(seq) - k)
        motifs.append(seq[rand_pos : rand_pos + k])

    best = motifs
    score_best = score(best)

    for j in range(N):
        i = random.randint(0, t - 1)

        motif_subset = motifs[:]
        motif_subset.pop(i)

        profile = profile_matrix(motif_subset, k)
        motifs[i] = profile_most_probable(dna[i], k, profile)

        score_motifs = score(motifs)
        if score_motifs < score_best:
            best = motifs
            score_best = score_motifs

    return best, score_best


def repeated_gibbs_sampler(dna, k, t, N, *, times=20):
    best, score_best = gibbs_sampler(dna, k, t, N)
    for _ in range(times - 1):
        new_best, new_score = gibbs_sampler(dna, k, t, N)
        if new_score < score_best:
            best = new_best
            score_best = new_score

    return best


result = repeated_gibbs_sampler(
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA".split(),
    8,
    5,
    100,
)
assert (
    score(result) <= score("CTCGGGGG CCAAGGTG TACAGGCG TTCAGGTG TCCACGTG".split()) + 1
), result


if __name__ == "__main__":
    with open("data/rosalind_ba2g.txt", "r") as dataset:
        k, t, N = [int(d) for d in dataset.readline().rstrip().split()]
        text = [l.rstrip() for l in dataset.readlines()]
    print(*repeated_gibbs_sampler(text, k, t, N), sep="\n")
