def ChromosomeToCycle(chromosome):
    nodes=[]
    for j in range(0,len(chromosome)):
        i=chromosome[j]
        if i>0:
            nodes.append(2*i-1)
            nodes.append(2*i)
        else:
            nodes.append(-2*i)
            nodes.append(-2*i-1)
    return nodes
            


def ColoredEdges(P):
    edges=[]
    for chromosome in P:
        nodes=ChromosomeToCycle(chromosome)
        for j in range(0,len(chromosome)):
            edges.append((nodes[2*j+1],nodes[(2*j+2)%len(nodes)]))
    return edges




x="""(+1 -2 -3)(+4 +5 -6)"""
x=x[1:-1]
p=x.split(")(")
chromosome=[]
for x in p:
    y=[int(z) for z in x.split(" ")]
    chromosome.append(y)
colored_edges=ColoredEdges(chromosome)
for i in range(0,len(colored_edges)):
    colored_edges[i]=str(colored_edges[i])
colored_edges=",".join(colored_edges)
print(colored_edges)

    
