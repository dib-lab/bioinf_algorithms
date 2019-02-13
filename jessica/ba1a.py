# Problem BA1A
# http://rosalind.info/problems/ba1a/

def PatternCount(Text, Pattern):
    count = 0
    overlap = len(Text) - len(Pattern) + 1
    for i in range(overlap):
        start = i
        end = i + len(Pattern)
        if Text[start:end] == Pattern:
            count = count + 1
    return(count)

# input
# PatternCount("GCGCG", "GCG")
# 2
