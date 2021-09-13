def kmer(text,i,k):
    return text[i:(i+k)]
def kmersfrequency(text,k):
    D=dict()
    for i in range(0,len(text)-k+1):
        tmp=kmer(text,i,k)
        try:
            D[tmp]=D[tmp]+1
        except KeyError:
            D[tmp]=1
    return D
def mostfrequentkmers(dictionary):
    L=list()
    for key,value in dictionary.items():
        if value==max(dictionary.values()):
            L.append(key)
    return L



x="""ACGTTGCATGTCGCATGATGCATGAGAGCT
4"""
inlines=x.split("\n")
text=inlines[0]
k=int(inlines[1])
D=kmersfrequency(text,k)
print(mostfrequentkmers(D))
