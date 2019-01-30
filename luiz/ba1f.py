#! /usr/bin/env python


def minimum_skew(genome):
    c_count = 0
    g_count = 0
    min_skew = 0
    mins = []

    for i, base in enumerate(genome):
        skew = g_count - c_count
        if skew < min_skew:
            min_skew = skew
            mins = [i]
        elif skew == min_skew:
            mins.append(i)

        if base == "C":
            c_count += 1
        elif base == "G":
            g_count += 1

    return mins


def minimum_skew_array(genome):
    c_count = 0
    g_count = 0
    skew = []

    for base in genome:
        skew.append(g_count - c_count)
        if base == "C":
            c_count += 1
        elif base == "G":
            g_count += 1

    min_skew = min(skew)
    return [i for (i, p) in enumerate(skew) if p == min_skew]


assert minimum_skew(
    "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
) == [53, 97]


if __name__ == "__main__":
    with open("data/rosalind_ba1f.txt", "r") as dataset:
        text = dataset.readline().rstrip()
    print(*minimum_skew(text))
