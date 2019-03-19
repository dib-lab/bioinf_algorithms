#! /usr/bin/env python

from ba1g import hamming
from ba2c import profile_most_probable


def profile_matrix(motifs, k):
    matrix = []
    for i in range(4):
        matrix.append([0.0] * k)

    n_motifs = len(motifs)
    for i in range(k):
        matrix[0][i] = sum(p[i].count("A") for p in motifs) / n_motifs
        matrix[1][i] = sum(p[i].count("C") for p in motifs) / n_motifs
        matrix[2][i] = sum(p[i].count("G") for p in motifs) / n_motifs
        matrix[3][i] = sum(p[i].count("T") for p in motifs) / n_motifs

    return matrix


def score(motifs):
    size = len(motifs[0])
    common_kmer = []
    for i in range(size):
        max_freq = 0
        pos_freq = dict(zip("ACGT", (0, 0, 0, 0)))
        for motif in motifs:
            nt = motif[i]
            pos_freq[nt] += 1
            max_freq = max(max_freq, pos_freq[nt])

        for nt, freq in pos_freq.items():
            if freq == max_freq:
                common_kmer.append(nt)
                break

        common = "".join(common_kmer)

    return sum(hamming(common, kmer) for kmer in motifs)


def greedy_motif_search(dna, k, t):
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
