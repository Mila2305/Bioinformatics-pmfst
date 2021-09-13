'''
Minimum Skew Problem

Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).

URL: http://rosalind.info/problems/ba1f/
'''
def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]
def skew(text):
    skew_array=[0]*(len(text)+1)
    for k in range (1,len(text)+1):
        if kmer(text,0,k)[-1]=='C':
            skew_array[k]=skew_array[k-1]-1
        else:
            if kmer(text,0,k)[-1]=='G':
                skew_array[k]=skew_array[k-1]+1
            else:
                skew_array[k]=skew_array[k-1]

    return (skew_array)
def index_min(skew):
    index_list=list()
    min_skew=min(skew)
    for i in range (0,len(skew)):
        if skew[i]==min_skew:
            index_list.append(i)
    return (index_list)

x="""CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"""
print(index_min(skew(x)))
