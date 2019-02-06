import sys
import argparse

def rev_complement(bases):
    complement= {'A':'T','T':'A','G':'C','C':'G'}
    rc_bases = ''
    for b in bases.upper():
        rc_bases+=complement[b]
    rc_bases = rc_bases[::-1]
    return rc_bases

assert rev_complement("AAAACCCGGT") == "ACCGGGTTTT"

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--bases', default='AAAACCCGGT')
    args = p.parse_args()
    sys.stdout.write(rev_complement(args.bases))
