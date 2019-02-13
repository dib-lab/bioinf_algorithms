# Problem BA1G
# http://rosalind.info/problems/ba1g/

def HammingDist(string1, string2):
    "This function calculates the number of mismatches between two strings of equal length."
    # set number of mismatches to 0
    number_mismatch = 0
    string_length = len(string1)
    # define length of strings to loop over
    for i in range(string_length):
        if string1[i] != string2[i]:
            number_mismatch += 1
    return number_mismatch

# input
# HammingDist("GGGCCGTTGGT", "GGACCGTTGAC")

# output
# 3


