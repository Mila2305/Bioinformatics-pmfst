def PatternToNumber(pattern):
    k=0
    num=0
    for x in pattern[::-1]:
        if x=="C":
            num=num+1*4**k
        if x=="G":
            num=num+2*4**k
        if x=="T":
            num=num+3*4**k
        k+=1
    return num

x="AGT"
print(PatternToNumber(x))
