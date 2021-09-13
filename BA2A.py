def kmer(text,i,k):
    return text[i:(i+k)]

def HammingDistance(p,q):
    if len(p)!=len(q):
        return -1
    count=0
    for first,second in zip(p,q):
        if first!=second:
            count+=1
    return count


def ApproximatePatternCount(text,pattern,d):
    count=0
    for i in range(0,len(text)-len(pattern)+1):
        if (HammingDistance(pattern,kmer(text,i,k))<=d):
            count=count+1
    return count

def suffix(pattern):
    return pattern[1:]

def Neighbors(pattern,d):
    nucleotides={"A","C","G","T"}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucleotides
    neighborhood=set()
    suffixNeighbors=Neighbors(suffix(pattern),d)
    for x in suffixNeighbors:
        if (HammingDistance(suffix(pattern),x)<d):
            for n in nucleotides:
                neighborhood.add(n+x)
        else:
            neighborhood.add(pattern[0]+x)
    return neighborhood

def Lwindows(text,L):
    windows=list()
    for i in range(0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows


def kmerswithapproxcount(text,k,d):
    D=dict()
    for windows in Lwindows(text,k):
        for pattern in Neighbors(windows,d):
            D[pattern]=ApproximatePatternCount(text,pattern,d)
    return D

def MotifEnumeration(dnalist,k,d):
    L=list()
    for dna in dnalist:
        L.append(kmerswithapproxcount(dna,k,d))
    RES=dict()
    for D in L:
        for k in D.keys():
            try:
                RES[k]=RES[k]+1
            except KeyError:
                RES[k]=1
    return [k for k,v in RES.items() if v==len(dnalist)]

x="""
3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT
"""
inlines=x.split()
k=int(inlines[0])
d=int(inlines[1])
dnalist=list()
for i in range(2,len(inlines)):
    dnalist.append(inlines[i])
result=MotifEnumeration(dnalist,k,d)
print(result)






            
























    
