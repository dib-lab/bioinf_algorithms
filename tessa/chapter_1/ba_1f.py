import sys
import argparse

# Find the minimum skew

def find_min_skew(genome):
    skew = [0]
    min_skew = 0
    min_skew_pos = []
    for b in genome:
       # if G, skew +1 
        if b.upper() == 'G': 
            skew_val = skew[-1] + 1
            skew+=[skew_val]
       # if C, skew -1, reassess minimum skew 
        elif b.upper() == 'C': 
            skew_val = skew[-1] - 1
            skew+=[skew_val]
            if skew_val == min_skew:
                min_skew_pos+= [len(skew)-1]
            elif skew_val < min_skew:
                min_skew = skew_val
                min_skew_pos = [len(skew)-1]
        else:
            # if A or T, add same skew_val to the list of skew_vals
            skew+=[skew_val]
    return(set(min_skew_pos))

assert find_min_skew("CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG") == set([53, 97])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--genome', default="CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG")
    args = p.parse_args()
    sys.stdout.write(" ".join(map(str,find_min_skew(args.genome))))
