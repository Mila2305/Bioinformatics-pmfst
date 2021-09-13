def get_genetic_code_codons():
    genetic_code={
                "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
        }
    return genetic_code


def kmer(text,i,k):
    return text[i:(i+k)]

def Lwindows(text,L):
    windows=list()
    for i in range(0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def DnaToRna(dna):
    rna=list()
    for i in range(0,len(dna)):
        if dna[i]=="T":
            rna.append("U")
        else:
            rna.append(dna[i])
    return "".join(rna)

def RnaToDna(rna):
    dna=list()
    for i in range(0,len(rna)):
        if rna[i]=="U":
            dna.append("T")
        else:
            dna.append(rna[i])
    return "".join(dna)

def reverse_complement(text):
    reverse=""
    for i in range(0,len(text)):
        if text[i]=="A":
            reverse+="U"
        if text[i]=="U":
            reverse+="A"
        if text[i]=="C":
            reverse+="G"
        if text[i]=="G":
            reverse+="C"
    return reverse[::-1]

def translation(rna):
    G=get_genetic_code_codons()
    res=list()
    for i in range(0,len(rna),3):
        letter=G[rna[i:i+3]]
        if letter=="*":
            break
        res.append(letter)
    return "".join(res)

def PeptideEncoding(dna,peptide):
    result=list()
    np=len(peptide)
    rna=DnaToRna(dna)
    for windows in Lwindows(rna,3*np):
        if translation(windows)==peptide:
            result.append(RnaToDna(windows))
    for windows in Lwindows(rna,3*np):
        if translation(reverse_complement(windows))==peptide:
            result.append(RnaToDna(windows))
    return result

x="""ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA"""
inlines=x.split()
dna=inlines[0]
peptide=inlines[1]
print(PeptideEncoding(dna,peptide))




    







        
