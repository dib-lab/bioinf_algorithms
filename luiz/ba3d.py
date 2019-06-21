#! /usr/bin/env python

from ba3c import overlap
from ba3a import composition


def de_bruijn(k, text):
    kmers = list(composition(k - 1, text))

    dbg = {}

    for kmer, neighbor in overlap(kmers):
        if kmer not in dbg:
            dbg[kmer] = set()

        dbg[kmer].add(neighbor)

    return dbg


assert de_bruijn(4, "AAGATTCTCTAC") == {
    "AAG": {"AGA"},
    "AGA": {"GAT"},
    "ATT": {"TTC"},
    "CTA": {"TAC"},
    "CTC": {"TCT"},
    "GAT": {"ATT"},
    "TCT": {"CTA", "CTC"},
    "TTC": {"TCT"},
}


if __name__ == "__main__":
    with open("data/rosalind_ba3d.txt", "r") as dataset:
        k = int(dataset.readline().strip())
        text = dataset.readline().strip()

    dbg = de_bruijn(k, text)

    for kmer, neighbors in dbg.items():
        if len(neighbors) == 1:
            print(kmer, "->", neighbors.pop())
        else:
            neighbors = list(neighbors)
            print(kmer, "->", neighbors[0], end="")
            for neighbor in neighbors[1:]:
                print(",{}".format(neighbor))
