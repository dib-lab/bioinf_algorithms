#! /usr/bin/env python


def approximate_pattern_match(text, pattern):
    matches = []
    for i in range(len(text) - len(pattern)):
        if text[i : i + len(pattern)] == pattern:
            matches.append(i)
    return matches


assert approximate_pattern_match("GATATATGCATATACTT", "ATAT") == [1, 3, 9]


if __name__ == "__main__":
    with open("data/rosalind_ba1d.txt", "r") as dataset:
        pattern = dataset.readline().rstrip()
        text = dataset.readline().rstrip()
    print(*approximate_pattern_match(text, pattern), sep=" ")
