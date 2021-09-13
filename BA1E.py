def kmer(text,i,k):
    return text[i:i+k]
def Lwindows(text,L):
    windows=[]
    for i in range(0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows
def kmersfrequency(text,k):
    D=dict()
    for i in range(0,len(text)-k+1):
        tmp=kmer(text,i,k)
        try:
            D[tmp]=D[tmp]+1
        except KeyError:
            D[tmp]=1
    return D
def kmersfrequency_t(D,t):
    L=[]
    for k,v in D.items():
        if v>=t:
            L.append(k)
    return L
def clumps(text,k,L,t):
    clumps=set()
    for window in Lwindows(text,L):
        x=kmersfrequency_t(kmersfrequency(window,k),t)
        for el in x:
            clumps.add(el)
    return clumps
x="""CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4"""
inlines=x.split("\n")
text=inlines[0]
inlines_1=inlines[1].split()
k=int(inlines_1[0])
L=int(inlines_1[1])
t=int(inlines_1[2])
print(clumps(text,k,L,t))

        
