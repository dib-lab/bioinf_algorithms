#! /usr/bin/env python


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            count += 1
    return count


assert pattern_count("GCGCG", "GCG") == 2


if __name__ == "__main__":
    with open("data/rosalind_ba1a.txt", "r") as dataset:
        text = dataset.readline().rstrip()
        pattern = dataset.readline().rstrip()
    print(pattern_count(text, pattern))
