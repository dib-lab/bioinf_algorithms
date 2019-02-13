# Problem BA1D
# http://rosalind.info/problems/ba1d/

def PatternMatchCount(Text, Pattern):
    # create empty list to store pattern locations in text
    match_spot = []
    # define length to search over
    overlap = len(Text) - len(Pattern) + 1
    for i in range(overlap):
        start = i
        end = i + len(Pattern)
        if Text[start:end] == Pattern:
            match_spot.append(i)
    return match_spot

# input
# PatternMatchCount("GATATATGCATATACTT", "ATAT")
# output
# [1, 3, 9]
