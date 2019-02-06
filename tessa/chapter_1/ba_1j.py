import sys
import argparse


def hamming_distance(patternA, patternB):
    h_dist = 0
    assert len(patternA) == len(patternB), 'please input strings of equal length'
    for i in range(len(patternA)):
        if patternA[i] !=patternB[i]:
            h_dist+=1
    return h_dist


def rev_complement(bases):
    complement= {'A':'T','T':'A','G':'C','C':'G'}
    rc_bases = ''
    for b in bases.upper():
        rc_bases+=complement[b]
    rc_bases = rc_bases[::-1]
    return rc_bases



def generate_mismatched_kmers(kmer, h_dist):
    mismatched_list = []
    if h_dist == 0:
        return [kmer]
    elif len(kmer) ==1:
        return ['A', 'G', 'C', 'T']
    #generate neighbor mismatches
    for neighbor in generate_mismatched_kmers(kmer[1:], h_dist):
        #print(kmer[1:])
        #print(neighbor)
        if hamming_distance(kmer[1:], neighbor) < h_dist:
            mismatched_list+=['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor]
        else:
            mismatched_list+=[kmer[0] + neighbor]
    return mismatched_list


def fuzzy_frequent_words(genome, ksize, num_mismatch):
    kmerD = {}
    for start in range(len(genome) - ksize + 1):
        kmer = genome[start: start + ksize]
        rc_kmer = rev_complement(kmer)
        mismatched_kmers = generate_mismatched_kmers(kmer, num_mismatch)
        mismatched_kmers.extend(generate_mismatched_kmers(rc_kmer, num_mismatch))
        for km in mismatched_kmers:
            if km in kmerD:
                kmerD[km] += 1
            else:
                kmerD[km] = 1
    maxCount = max(kmerD.values())
    freqKmers= [kmer for kmer, count in kmerD.items() if count == maxCount]
    return freqKmers


assert set(fuzzy_frequent_words("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)) == set(["ATGT","ACAT"])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--genome', default='ACGTTGCATGTCGCATGATGCATGAGAGCT')
    p.add_argument('-k', '--ksize', type=int, default=4)
    p.add_argument('-d', '--num_mismatches', type=int, default=1)
    args = p.parse_args()
    sys.stdout.write(" ".join(map(str,fuzzy_frequent_words(args.genome, args.ksize, args.num_mismatches))))
