import sys
import argparse

def hamming_distance(patternA, patternB):
    h_dist = 0
    assert len(patternA) == len(patternB), 'please input strings of equal length'
    for i in range(len(patternA)): 
        if patternA[i] !=patternB[i]:
            h_dist+=1
    return h_dist

assert hamming_distance("GGGCCGTTGGT","GGACCGTTGAC") == 3

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--patternA', default='GGGCCGTTGGT')
    p.add_argument('--patternB', default='GGACCGTTGAC')
    args = p.parse_args()
    sys.stdout.write(str(hamming_distance(args.patternA, args.patternB)))
