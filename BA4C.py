def get_amino_acid_mass():
    mass={
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,


    }
    return mass

def spectrum(peptide):
    rez=[]
    D=get_amino_acid_mass()
    rez.append(0)
    rez.append(sum([D[x] for x in peptide]))
    extended_peptide=peptide+peptide[:-1]
    for i in range(0,len(peptide)):
        for k in range(1,len(peptide)):
            subpeptide=peptide[i:(i+k)]
            rez.append(sum([D[x] for x in subpeptide]))
    return sorted(rez)
    
    
    
x="""LEQN"""
print(spectrum(x))


