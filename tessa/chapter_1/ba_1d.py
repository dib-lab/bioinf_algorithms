import sys
import argparse

def locate_pattern(bases, pattern):
    locations = []
    for start in range(len(bases) - len(pattern) + 1):
        if bases[start: start + len(pattern)] == pattern:
            locations.append(start)
        start+=1
    return locations

assert locate_pattern("GATATATGCATATACTT", "ATAT") == [1,3,9] 

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--bases', default="GATATATGCATATACTT")
    p.add_argument('-p', '--pattern', default= "ATAT")
    args = p.parse_args()
    sys.stdout.write(" ".join(map(str,locate_pattern(args.bases, args.pattern))))
