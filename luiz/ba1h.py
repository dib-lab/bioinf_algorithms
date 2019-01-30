#! /usr/bin/env python


from ba1g import hamming


def approximate_pattern_match(text, pattern, distance):
    matches = []
    for i in range(len(text) - len(pattern)):
        if hamming(text[i : i + len(pattern)], pattern) <= distance:
            matches.append(i)
    return matches


assert approximate_pattern_match(
    "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC",
    "ATTCTGGA",
    3,
) == [6, 7, 26, 27, 78]


if __name__ == "__main__":
    with open("data/rosalind_ba1h.txt", "r") as dataset:
        pattern = dataset.readline().rstrip()
        text = dataset.readline().rstrip()
        dist = int(dataset.readline().rstrip())
    print(*approximate_pattern_match(text, pattern, dist), sep=" ")
