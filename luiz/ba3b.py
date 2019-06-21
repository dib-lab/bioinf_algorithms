#! /usr/bin/env python


def genome_from_path(kmers):
    joined = [kmers[0]]
    for kmer in kmers[1:]:
        joined.append(kmer[-1])

    return "".join(joined)


assert genome_from_path("ACCGA CCGAA CGAAG GAAGC AAGCT".split()) == "ACCGAAGCT"


if __name__ == "__main__":
    with open("data/rosalind_ba3b.txt", "r") as dataset:
        text = [l.rstrip() for l in dataset.readlines()]
    print(genome_from_path(text))
