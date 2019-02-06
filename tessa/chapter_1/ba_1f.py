import sys
import argparse

# Find the minimum skew

def find_min_skew(genome):
    skew_val = 0
    min_skew = 0
    min_skew_pos = []
    for i, b in enumerate(genome,1):
        if b.upper() == 'G':
            skew_val = skew_val + 1
        elif b.upper() == 'C':
            skew_val = skew_val - 1
            if skew_val == min_skew:
                min_skew_pos.append(i)       
            elif skew_val < min_skew:
                min_skew = skew_val
                min_skew_pos = [i]
    return min_skew_pos


assert find_min_skew("CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG") == set([53, 97])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--genome', default="CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG")
    args = p.parse_args()
    sys.stdout.write(" ".join(map(str,find_min_skew(args.genome))))
