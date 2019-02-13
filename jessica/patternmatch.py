def PatternMatch(Text, Pattern):
    overlap = len(Text) - len(Pattern) + 1
    starts = []
    for i in range(overlap):
        start = i
        end = i + len(Pattern)
        if Text[start:end] == Pattern:
            starts.append(start) 
    return(starts)

# input
# PatternMatch("GATATATGCATATACTT", "ATAT")
# output [1, 3, 9]

