def NumberToPattern(index,k):
    pattern=""
    D={0:"A",1:"C",2:"G",3:"T"}
    q=index
    for i in range(0,k):
        r=q%4
        q=q//4
        pattern=pattern+D[r]
    return pattern[::-1]
    
x="""45
4"""
inlines=x.split("\n")
index=int(inlines[0])
k=int(inlines[1])
print(NumberToPattern(index,k))
