#! /usr/bin/env python


def composition(k, text):
    for i in range(len(text) - k + 1):
        yield text[i : i + k]


assert set(composition(5, "CAATCCAAC")) == {"AATCC", "ATCCA", "CAATC", "CCAAC", "TCCAA"}

if __name__ == "__main__":
    with open("data/rosalind_ba3a.txt", "r") as dataset:
        k = int(dataset.readline().rstrip())
        text = dataset.readline().rstrip()
    print(*composition(k, text), sep="\n")
