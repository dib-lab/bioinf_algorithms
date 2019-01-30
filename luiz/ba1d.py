#! /usr/bin/env python


def pattern_count(text, pattern):
    matches = []
    for i in range(len(text) - len(pattern)):
        if text[i : i + len(pattern)] == pattern:
            matches.append(i)
    return matches


assert pattern_count("GATATATGCATATACTT", "ATAT") == [1, 3, 9]


if __name__ == "__main__":
    with open("data/rosalind_ba1d.txt", "r") as dataset:
        pattern = dataset.readline().rstrip()
        text = dataset.readline().rstrip()
    print(*pattern_count(text, pattern), sep=" ")
