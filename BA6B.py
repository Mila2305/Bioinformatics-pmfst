def breakpoints(str_permutation):
    n=len(str_permutation.split(" "))
    helper="0 "+str_permutation[1:-1]+" "+str(n+1)
    int_permutation=[int(x) for x in helper.split(" ")]
    n_breakpoints=0
    for i in range(1,n+2):
        if int_permutation[i]-int_permutation[i-1]!=1:
            n_breakpoints+=1
    return n_breakpoints
            



x="""(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"""
print(breakpoints(x))
