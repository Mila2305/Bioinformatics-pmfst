"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Compute the Number of Times a Pattern Appears in a Text
Rosalind ID: BA1A
URL: http://rosalind.info/problems/ba1a/
"""

def kmer(text,i,k):
    return text[i:(i+k)]

def PatternCount(text,pattern):
    count=0
    for i in range(0,len(text)-len(pattern)+1):
        if kmer(text,i,len(pattern))==pattern:
            count+=1
    return count

x="""GCGCG
GCG"""
inlines=x.split("\n")
text=inlines[0]
pattern=inlines[1]
print(PatternCount(text,pattern))
