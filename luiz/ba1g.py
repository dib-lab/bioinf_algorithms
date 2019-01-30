#! /usr/bin/env python


def hamming(A, B):
    return sum(1 for Ac, Bc in zip(A, B) if Ac != Bc)


assert hamming("GGGCCGTTGGT", "GGACCGTTGAC") == 3


if __name__ == "__main__":
    with open("data/rosalind_ba1g.txt", "r") as dataset:
        seq1 = dataset.readline().rstrip()
        seq2 = dataset.readline().rstrip()
    print(hamming(seq1, seq2))
