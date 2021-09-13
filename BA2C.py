def kmer(text,i,k):
    return text[i:(i+k)]

def Lwindows(text,L):
    windows=list()
    for i in range(0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def probability(window,profile):
    prob=1
    for i in range(0,len(window)):
        if window[i]=="A":
            prob=prob*profile[0][i]
        else:
            if window[i]=="C":
                prob=prob*profile[1][i]
            else:
                if window[i]=="G":
                    prob=prob*profile[2][i]
                else:
                    if window[i]=="T":
                        prob=prob*profile[3][i]
    return prob

def mostProbkmerinText(text,k,profile):
    d=dict()
    for window in Lwindows(text,k):
        d[window]=probability(window,profile)
    return [x[0] for x in d.items() if x[1]==max(d.values())][0]

x="""ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2"""

inlines=x.split("\n")
text=inlines[0]
k=int(inlines[1])
profile=list()
for i in range(2,6):
    profile.append(inlines[i].split())
    for j in range(0,k):
        profile[i-2][j]=float(profile[i-2][j])
res=mostProbkmerinText(text,k,profile)
print(res)
