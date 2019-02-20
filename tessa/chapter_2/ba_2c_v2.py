import sys
import argparse

## faster: store kmer + probabilities in a list of tuples (instead of dictionary)! 

def calculate_probability(kmer, prob_matrix):
    p = 1 
    for i, base in enumerate(kmer):
        p += float(prob_matrix[base][i])
    return p

def profile_most_probable(dna, ksize, motif_matrix):
    kmer_prob = []
    for i in range(len(dna) - ksize + 1):
        kmer = dna[i:i+ksize]
        kmer_prob.append((calculate_probability(kmer, motif_matrix), kmer))
    kmer_prob.sort() # sort the list in place
    return kmer_prob[-1][1]

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--data', default="data/rosalind_ba2c.txt")
    args = p.parse_args()
    with open(args.data, "r") as d:
        dna_str = d.readline().strip()
        ksize = int(d.readline().strip())
        p_matrix = {}
        p_matrix['A'] = d.readline().rstrip().split(' ')
        p_matrix['C'] = d.readline().rstrip().split(' ')
        p_matrix['G'] = d.readline().rstrip().split(' ')
        p_matrix['T'] = d.readline().rstrip().split(' ')
        print(profile_most_probable(dna_str, ksize, p_matrix))
