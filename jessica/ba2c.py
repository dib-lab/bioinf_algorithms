# Problem BA2C
# http://rosalind.info/problems/ba2c/

import operator

def ProfProbKmer(Text, k, ProfileMatrix):
    searchable_kmer = []
    matrix_length = k
    A_profile = list(ProfileMatrix[0].split())
    C_profile = list(ProfileMatrix[1].split())
    G_profile = list(ProfileMatrix[2].split())
    T_profile = list(ProfileMatrix[3].split())

    # Assume all profile lengths are the same
    for position in range(k):
        # Create dictionary of probability values at each nucleotide position
        nucleotide_values_position = {}
        nucleotide_values_position.update({'A' : A_profile[position], 'C' : C_profile[position], 'G' : G_profile[position], 'T' : T_profile[position]})
        
        # get max value of each position from specific dictionary
        highest_freq = max(nucleotide_values_position.items(), key = operator.itemgetter(1))[0]
        searchable_kmer.append(highest_freq)
    
    searchable_kmer_str = "".join(searchable_kmer)
    return searchable_kmer_str
    

