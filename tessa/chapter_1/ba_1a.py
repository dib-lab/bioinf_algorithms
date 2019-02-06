import sys
import argparse

def pattern_count(bases, pattern):
    count = 0
    for start in range(len(bases) - len(pattern) + 1):
        if bases[start: start + len(pattern)] == pattern:
            count += 1
        start+=1
    sys.stdout.write(str(count))
    return count

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--bases', default='GCGCG')
    p.add_argument('-p', '--pattern', default= 'GCG')
    args = p.parse_args()
    sys.exit(pattern_count(args.bases, args.pattern))
