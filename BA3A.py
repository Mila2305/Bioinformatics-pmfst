def kmerComposition(text,k):
    kmerarray=[]
    for i in range(0,len(text)-k+1):
        kmerarray.append(text[i:(i+k)])
    return sorted(kmerarray)

x="""5
CAATCCAAC"""
inlines=x.split()
k=int(inlines[0])
text=inlines[1]
print(kmerComposition(text,k))
