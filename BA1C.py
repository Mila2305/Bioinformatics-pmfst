"""
Reverse Complement Problem

Find the reverse complement of a DNA string.

Given: A DNA string Pattern.

Return: Pattern, the reverse complement of Pattern.

URL: http://rosalind.info/problems/ba1c/
"""

def ReverseComplement(pattern):
    reverse=""
    for i in range(0,len(pattern)):
        if pattern[i]=="G":
            reverse=reverse+"C"
        elif pattern[i]=="C":
            reverse=reverse+"G"
        elif pattern[i]=="T":
            reverse=reverse+"A"
        elif pattern[i]=="A":
            reverse=reverse+"T"
    return reverse[::-1]

x="""AAAACCCGGT"""
print(ReverseComplement(x))
    
