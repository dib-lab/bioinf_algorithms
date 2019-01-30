#! /usr/bin/env python

from ba1a import pattern_count


def frequent_words(text, k):
    frequent_patterns = set()
    count = {}
    for i in range(len(text) - k):
        pattern = text[i : i + k]
        count[i] = pattern_count(text, pattern)
        max_count = max(count.values())

    for i in range(len(text) - k):
        if count[i] == max_count:
            frequent_patterns.add(text[i : i + k])

    return frequent_patterns


assert frequent_words("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4) == set("CATG GCAT".split())


if __name__ == "__main__":
    with open("data/rosalind_ba1b.txt", "r") as dataset:
        text = dataset.readline().rstrip()
        k = int(dataset.readline().rstrip())
    print(*frequent_words(text, k))
