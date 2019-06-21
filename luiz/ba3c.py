#! /usr/bin/env python


def overlap(kmers):
    adj_list = {}

    for kmer in kmers:
        neighbors = []

        for other in kmers:
            if other == kmer:
                continue
            elif kmer[1:] == other[:-1]:
                neighbors.append(other)

        adj_list[kmer] = neighbors

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            yield (node, neighbor)


assert set(overlap("ATGCG GCATG CATGC AGGCA GGCAT".split())) == set(
    [("AGGCA", "GGCAT"), ("CATGC", "ATGCG"), ("GCATG", "CATGC"), ("GGCAT", "GCATG")]
)


if __name__ == "__main__":
    with open("data/rosalind_ba3c.txt", "r") as dataset:
        text = [l.rstrip() for l in dataset.readlines()]

    for start, end in sorted(overlap(text)):
        print(start, "->", end)
