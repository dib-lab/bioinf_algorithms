# Problem BA2A
# http://rosalind.info/problems/ba2a/

def HammingDist(string1, string2):
    "This function calculates the number of mismatches between two strings of equal length."
    # check if strings are same length
    #assert len(string1) == len(string2), "Strings must be the same length!"
    if len(string1) != len(string2):
        raise ValueError("Strings must be the same length!")
    # set number of mismatches to 0
    number_mismatch = 0
    string_length = len(string1)
    # define length of strings to loop over
    for i in range(string_length):
        if string1[i] != string2[i]:
            number_mismatch += 1
    return number_mismatch

def CreateKmers(kmer, d):
    "This function creates all possible kmers in the string Dna of length k"
    new_kmers = []
    if d == 0:
        # why is this in brackets
        return [kmer]
    elif len(kmer) == d:
        return ['A', 'G', 'C', 'T']
    # generate mismatches
    for neighbor in CreateKmers(kmer[1:], d):
        if HammingDist(kmer[1:], d) < d:
            new_kmers.append('A' + neighbor, 'C' + neighbor, 'G' + neighbor, 'T' + neighbor)
        else:
            new_kmers.append(kmer[0] + neighbor)
    return new_kmers

def MotifEnumeration(Dna, k, d):
    "Dna = strings of DNA all MUST be the same length, k = length of kmer, d = max number of mismatches"
    # Store each DNA string in library
    Dna_strings = []
    for line in DNA:
        Dna_strings.append(line)
    # Create list of patterns satisfying requirements
    Final_kmers = []
    # iterate through each Dna string, j = Dna string in list
    for j in Dna_strings:
        kmers_in_'j' = {}
        overlap = len(Dna_strings[j]) - k + 1
        for i in overlap:
            kmer = Dna[i:i+k]
            mispaired_kmers = CreateKmers(kmer, d)
            # iterate through possible kmers, add to dictionary of possible final patterns
                for possible_kmer in mispaired_kmers:
                    if possible_kmer in kmers_in_'j':
                        kmers_in_'j'.append([possible_kmer])
                    else:
                        kmers_in_'j'.append([possible_kmer])
                        
    # check if Keys in kmers_in_'j' appear in each line
    for list_of_kmers in kmers_in_*:
        set(kmers_in_'list_of_kmers')
        
