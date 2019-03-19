#! /usr/bin/env python

from ba2c import profile_most_probable
from ba2d import score


def profile_matrix(motifs, k):
    matrix = []
    for i in range(4):
        matrix.append([0.0] * k)

    n_motifs = len(motifs) + 4
    for k_pos in range(k):
        for nt_pos, nt in enumerate("ACGT"):
            pos_count = (sum(motif[k_pos].count(nt) for motif in motifs) + 1) / n_motifs
            matrix[nt_pos][k_pos] = pos_count

    return matrix


def greedy_motif_search_with_pseudocounts(dna, k, t):
    best = [t[:k] for t in dna]
    score_best = score(best)
    first = dna[0]

    for i in range(len(first) - k + 1):
        motif = first[i : i + k]
        motifs = [motif]
        for j in range(1, t):
            current = dna[j]
            profile = profile_matrix(motifs, k)
            motifs_j = profile_most_probable(current, k, profile)
            motifs.append(motifs_j)

        score_motifs = score(motifs)
        if score_motifs < score_best:
            best = motifs
            score_best = score_motifs

    return best


assert (
    greedy_motif_search_with_pseudocounts(
        "GGCGTTCAGGCA AAGAATCAGTCA CAAGGAGTTCGC CACGTCAATCAC CAATAATATTCG".split(), 3, 5
    )
    == "TTC ATC TTC ATC TTC".split()
)

if __name__ == "__main__":
    with open("data/rosalind_ba2e.txt", "r") as dataset:
        k, t = [int(d) for d in dataset.readline().rstrip().split()]
        text = [l.rstrip() for l in dataset.readlines()]
    print(*greedy_motif_search_with_pseudocounts(text, k, t))
