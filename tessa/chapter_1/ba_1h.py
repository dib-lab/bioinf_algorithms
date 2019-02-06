import sys
import argparse


def hamming_distance(patternA, patternB):
    h_dist = 0
    assert len(patternA) == len(patternB), 'please input strings of equal length'
    for i in range(len(patternA)):
        if patternA[i] !=patternB[i]:
            h_dist+=1
    return h_dist

def find_fuzzy_pattern(genome, pattern, num_mismatch):
    pattern_starts = []
    for p_start in range(len(genome) - len(pattern) +1):
        kmer = genome[p_start: p_start + len(pattern)]
        if kmer == pattern: # not really necessary(hamming dist gets this case) but maybe faster?
            pattern_starts+=[p_start]
        elif hamming_distance(pattern, kmer) <= num_mismatch:
            pattern_starts+=[p_start]
    return pattern_starts

assert set(find_fuzzy_pattern("CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC", "ATTCTGGA", 3)) == set([6,7,26,27,78])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--genome', default='CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC')
    p.add_argument('-p', '--pattern', default="ATTCTGGA")
    p.add_argument('-d', '--num_mismatches', type=int, default=3)
    args = p.parse_args()
    sys.stdout.write(" ".join(map(str,find_fuzzy_pattern(args.genome, args.pattern, args.num_mismatches))))
