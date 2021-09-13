"""
Pattern Matching Problem

Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.

URL: http://rosalind.info/problems/ba1d/
"""
def kmer(text,i,k):
    """substring of the text from i-th position for the next k letters"""
    return text[i:(i+k)]

def patterncountoccurences(text,pattern):
    occurences=[]
    np=len(pattern)
    for i in range(0,len(text)-np+1):
        if kmer(text,i,np)==pattern:
            occurences.append(i)
    return occurences

x="""ATAT
GATATATGCATATACTT"""
inlines=x.split("\n")
text=inlines[1]
pattern=inlines[0]
print(patterncountoccurences(text,pattern))
