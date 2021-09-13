def kmer(text,i,k):
    return text[i:(i+k)]

def kmersfrequency(text,k):
    D=dict()
    for i in range(0,len(text)-k+1):
        tmp=kmer(text,i,k)
        try:
            D[tmp]+=1
        except KeyError:
            D[tmp]=1
    return D

def HammingDistance(p,q):
    if len(p)!=len(q):
        return -1
    dist=0
    for first,second in zip(p,q):
        if first!=second:
            dist+=1
    return dist

def minHamm(text,pattern):
    D=kmersfrequency(text,len(pattern))
    return (min([(HammingDistance(pattern,x)) for x in D.keys()]))

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

def kmerNeighbors(text,k):
    L=set()
    for i in range(0,len(text)-k+1):
        for d in range(0,k+1):
            L.update(Neighbors(kmer(text,i,k),d))
    D=dict()
    for l in L:
        D[l]=minHamm(text,l)
    return D


def MedianString(dnalist,k):
    L=[]
    for dna in dnalist:
        L.append(kmerNeighbors(dna,k))
    s=set()
    for x in L:
        s=s.union(x.keys())
    RES=dict()
    for key in s:
        RES[key]=0
    for D in L:
        for key,value in D.items():
            RES[key]=RES[key]+value
    mincount=min([value for value in RES.values()])
    return ([key for key,value in RES.items() if mincount==value][0])
































