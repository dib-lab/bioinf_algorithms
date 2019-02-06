import sys
import argparse

def find_clumps(bases, clumpLen, ksize, numInClump):
    kmerD = {}
    for k_start in range(len(bases) - ksize + 1):
        kmer = bases[k_start: k_start + ksize]
        if kmer in kmerD.keys():
            kmerD[kmer]+=[k_start]
        else:
            kmerD[kmer] = [k_start]

    clumped_kmers = []
    for k, starts in kmerD.items():
        # slide a window length num across starts, figure out if starts[i + numInClump-1] - starts[i] <= 25
        for i in range(len(starts) - (numInClump-1)):
            dist = starts[i + numInClump-1] - starts[i] + ksize 
            if dist <= (clumpLen-ksize): # need to subtract ksize bc we're just considering starts 
                clumped_kmers+=[k]
    return set(clumped_kmers)

assert find_clumps("CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC", 25, 5 ,3) == set(['CGACA', 'GAAGA', 'AATGT'])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--bases', default="CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC")
    p.add_argument('--num', type=int, default= 3)
    p.add_argument('--ksize', type=int, default= 5)
    p.add_argument('--clump_length', type=int, default= 25)
    args = p.parse_args()
    sys.stdout.write(" ".join(map(str,find_clumps(args.bases, args.clump_length, args.ksize, args.num))))
