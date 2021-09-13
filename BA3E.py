def prefix(pattern):
    """substring of pattern without last letter"""
    return pattern[0:len(pattern)-1]

def sufix(pattern):
    """subrstring of pattern without first letter"""
    return pattern[1:len(pattern)]

def DeBruijnRec(Patterns):
    dictionary_nodes=dict()
    sortedPattern=sorted(Patterns)
    for pattern in sortedPattern:
        dictionary_nodes[prefix(pattern)]=[]
    for pattern in sortedPattern:
        dictionary_nodes[prefix(pattern)].append(sufix(pattern))
    return dictionary_nodes

x="""GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG"""

inlines=x.split()
kmers=[]
for i in range(0,len(inlines)):
    kmers.append(inlines[i])
dictionary_nodes=DeBruijnRec(kmers)
for key in dictionary_nodes.keys():
    print(key,"->",",".join(dictionary_nodes[key]))
