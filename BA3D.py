def deBruijnGraph(k,text):
    D={}
    for i in range(0,len(text)-k+1):
        first=text[i:(i+k-1)]
        second=text[(i+1):(i+k)]
        print(first)
        print(second)
        if first not in D:
            D[first]=[second]
        else:
            D[first].append(second)
    return D

x="""4
AAGATTCTCTAC"""

inlines=x.split()
k=int(inlines[0])
text=inlines[1]
dictionary_deBruijn=deBruijnGraph(k,text)
result=""
keys=sorted(dictionary_deBruijn.keys())
for first in keys:
    second=",".join(sorted(dictionary_deBruijn[first]))
    result=result+ f"{first} -> {second}\n"
print(result)
