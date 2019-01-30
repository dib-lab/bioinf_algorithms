#! /usr/bin/env python


TRANSLATION = {"A": "T", "C": "G", "G": "C", "T": "A"}


def revc(pattern):
    return "".join(TRANSLATION[c] for c in reversed(pattern))


assert revc("AAAACCCGGT") == "ACCGGGTTTT"


if __name__ == "__main__":
    with open("data/rosalind_ba1c.txt", "r") as dataset:
        text = dataset.readline().rstrip()
    print(revc(text))
