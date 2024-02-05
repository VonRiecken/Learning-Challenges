def dna_to_rna(dna):
    rna = []
    for i in dna:
        if i == 'G':
            rna.append('G')
        elif i == 'C':
            rna.append('C')
        elif i == 'T':
            rna.append('U')
        elif i == 'A':
            rna.append('A')
    return ''.join(rna)
