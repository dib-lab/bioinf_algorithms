def FindClumps(Genome, kmer_length, clump_length, times):
    # define Length to search within
    clump_overlap = len(Genome) - clump_length + 1
    # kmer_overlap is looking within clump
    kmer_overlap = clump_length - kmer_length + 1
    # define kmers greater than times
    keepers = set()
    for clump_index in range(clump_overlap):
        # define clump window
        clump_start = clump_index
        clump_end = clump_index + clump_length
        clump = Genome[clump_start:clump_end]
        # define dictionary of kmers
        kmer_counts = {}
        for kmer_index in range(kmer_overlap):
            kmer_start = kmer_index
            kmer_end = kmer_index + kmer_length
            kmer = clump[kmer_start:kmer_end]
            if kmer in kmer_counts:
                # if kmer in dictionary, add count, +=
                kmer_counts[kmer] = kmer_counts[kmer] + 1
            else:
                # if kmer not in dictionary, add it
                kmer_counts[kmer] = 1
        # check if kmers occur greater than times
        for kmer in kmer_counts:
            if kmer_counts[kmer] >= times:
                keepers.add(kmer)
    return keepers

# input
# FindClumps("CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC", 5, 75, 4)

# output
# {'AATGT', 'CGACA', 'GAAGA'}
