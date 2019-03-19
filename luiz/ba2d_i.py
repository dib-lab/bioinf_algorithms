#! /usr/bin/env python

from ba1g import hamming
from ba2c import profile_most_probable


def profile(motifs, k):
    matrix = []
    for i in range(4):
        matrix.append([0.0] * k)

    n_motifs = len(motifs)
    for i in range(k):
        motif_count = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            motif_count["A"] += motif[i].count("A")
            motif_count["C"] += motif[i].count("C")
            motif_count["G"] += motif[i].count("G")
            motif_count["T"] += motif[i].count("T")

        matrix[0][i] = motif_count["A"] / n_motifs
        matrix[1][i] = motif_count["C"] / n_motifs
        matrix[2][i] = motif_count["G"] / n_motifs
        matrix[3][i] = motif_count["T"] / n_motifs

    return matrix


def score(motifs):
    k = len(motifs[0])

    consensus = []

    for i in range(k):
        freq = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            freq["A"] += motif[i].count("A")
            freq["C"] += motif[i].count("C")
            freq["G"] += motif[i].count("G")
            freq["T"] += motif[i].count("T")

        max_freq = max(freq.values())
        for nt, count in freq.items():
            if count == max_freq:
                consensus.append(nt)
                break

    consensus = "".join(consensus)
    score_value = 0
    for motif in motifs:
        score_value += hamming(consensus, motif)

    return score_value


def greedy_motif_search(dna, k, t):
    # best_motifs = []
    # for seq in dna:
    #     first = seq[0:k]
    #     best_motifs.append(first)

    best_motifs = [seq[:k] for seq in dna]

    first_seq = dna[0]
    overlap = len(first_seq) - k + 1
    for start in range(overlap):
        kmer = first_seq[start : start + k]
        motif = [kmer]

        for i in range(1, t):
            matrix = profile(motif, k)
            most_probable = profile_most_probable(dna[i], k, matrix)
            motif.append(most_probable)

        if score(motif) < score(best_motifs):
            best_motifs = motif

    return best_motifs


assert (
    greedy_motif_search(
        "GGCGTTCAGGCA AAGAATCAGTCA CAAGGAGTTCGC CACGTCAATCAC CAATAATATTCG".split(), 3, 5
    )
    == "CAG CAG CAA CAA CAA".split()
)


if __name__ == "__main__":
    with open("data/rosalind_ba2d.txt", "r") as dataset:
        k, t = [int(d) for d in dataset.readline().rstrip().split()]
        text = [l.rstrip() for l in dataset.readlines()]
    print(*greedy_motif_search(text, k, t))
