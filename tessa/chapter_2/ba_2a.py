import sys
import argparse

def hamming_distance(patternA, patternB):
    h_dist = 0
    assert len(patternA) == len(patternB), 'please input strings of equal length'
    for i in range(len(patternA)):
        if patternA[i] !=patternB[i]:
            h_dist+=1
    return h_dist

def generate_mismatched_kmers(kmer, h_dist):
    mismatched_list = []
    if h_dist == 0:
        return [kmer]
    elif len(kmer) ==1:
        return ['A', 'G', 'C', 'T']
    for neighbor in generate_mismatched_kmers(kmer[1:], h_dist):
        if hamming_distance(kmer[1:], neighbor) < h_dist:
            mismatched_list+=['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor]
        else:
            mismatched_list+=[kmer[0] + neighbor]
    return mismatched_list

def motif_enumeration(dna_patterns, ksize, distance):
    patterns = set()
    first =  dna_patterns[0]
    for i in range(len(first) - ksize + 1): # for each kmer in the first dna pattern
        pattern = first[i: i + ksize] #kmer
        for new_pat in generate_mismatched_kmers(pattern, distance):
            patterns.add(new_pat)

    for dna_pat in dna_patterns[1:]: # look through the remaining dna patterns
        current_patterns=set()
        for i in range(len(dna_pat) - ksize +1): # for each kmer
            for pat in patterns:
                if hamming_distance(dna_pat[i:i+ksize], pat) <= distance:
                    current_patterns.add(pat)
        patterns = patterns.intersection(current_patterns)

    return patterns

assert set(motif_enumeration(["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"], 3, 1)) == set(["ATA","ATT","GTT","TTT"])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--dna', type=list, default=["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"])
    p.add_argument('-k', '--ksize', type=int, default=3)
    p.add_argument('-d', '--num_mismatches', type=int, default=1)
    args = p.parse_args()
    sys.stdout.write(" ".join(map(str,motif_enumeration(args.dna, args.ksize, args.num_mismatches))))
