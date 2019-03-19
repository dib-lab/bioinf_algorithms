#! /usr/bin/env python


def kmer_prob(kmer, matrix):
    prob = 1.0
    pos = dict(zip("ACGT", range(4)))
    for i, nt in enumerate(kmer):
        prob *= matrix[pos[nt]][i]
    return prob


def profile_most_probable(text, k, matrix):
    most_probable_kmer = None
    max_prob = 0
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        prob = kmer_prob(kmer, matrix)
        if most_probable_kmer is None:
            most_probable_kmer = kmer
            max_prob = prob
        elif prob > max_prob:
            most_probable_kmer = kmer
            max_prob = prob

    return most_probable_kmer


assert (
    profile_most_probable(
        "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT",
        5,
        [
            [0.2, 0.2, 0.3, 0.2, 0.3],
            [0.4, 0.3, 0.1, 0.5, 0.1],
            [0.3, 0.3, 0.5, 0.2, 0.4],
            [0.1, 0.2, 0.1, 0.1, 0.2],
        ],
    )
    == "CCGAG"
)


if __name__ == "__main__":
    with open("data/rosalind_ba2c.txt", "r") as dataset:
        text = dataset.readline().rstrip()
        k = int(dataset.readline().rstrip())
        matrix = []
        for s in dataset.readlines():
            matrix.append([float(f) for f in s.rstrip().split()])
    print(profile_most_probable(text, k, matrix))
