def ChromosomeToCycle(Chromosome):
    nodes=[]
    for j in range(0,len(Chromosome)):
        i=Chromosome[j]
        if i>0:
            nodes.append(2*i-1)
            nodes.append(2*i)
        else:
            nodes.append(-2*i)   #we want positive integer for nodes so if i is negative we must multiply with -1
            nodes.append(-2*i-1)
    return nodes

def RosalindPrint(L):
    s=""
    for x in L:
        s=s+str(x)+" "
    s="("+s[:-1]+")"
    return s
    

x="""(+1 -2 -3 +4)"""
chromosome=[int(x) for x in x[1:-1].split(" ")]
#print(chromosome)
#print(ChromosomeToCycle(chromosome))
print(RosalindPrint(ChromosomeToCycle(chromosome)))
