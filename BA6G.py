def CycleToChromosome(str_nodes):
    nodes=[int(x) for x in str_nodes[1:-1].split(" ")]
    k=int(len(nodes)/2)
    L=[]
    for i in range(0,k):
        if nodes[2*i]<nodes[2*i+1]:
            L.append(int(nodes[2*i+1]/2))
        else:
            L.append(int(-1*(nodes[2*i]/2)))
    return L

def RosalindPrint(L):
    s="("
    for x in L:
        if x>0:
            s=s+"+"+str(x)+" "
        else:
            s=s+str(x)+" "
        
    s=s[:-1]+")"
    return s
    

x="""(1 2 4 3 6 5 7 8)"""
print(CycleToChromosome(x))
print(RosalindPrint(CycleToChromosome(x)))
