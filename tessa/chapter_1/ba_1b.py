import sys
import argparse

def frequent_kmers(bases, ksize):
    kmerD = {}
    for start in range(len(bases) - ksize + 1):
        kmer = bases[start: start + ksize]
        if kmer in kmerD:
            kmerD[kmer] = kmerD[kmer] + 1
        else:
            kmerD[kmer] = 1
    maxCount=0
    freqKmers= []
    for kmer,count in kmerD.items():
        if count > maxCount:
            maxCount = count
            freqKmers = [kmer]
        elif count == maxCount:
            freqKmers+=[kmer]
    return freqKmers

# assertion idea swiped from luiz!
assert set(frequent_kmers("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)) == set("CATG GCAT".split())

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--bases', default='ACGTTGCATGTCGCATGATGCATGAGAGCT')
    p.add_argument('-k', '--ksize', type=int, default=4)
    args = p.parse_args()
    sys.stdout.write(' '.join(frequent_kmers(args.bases, args.ksize)))
