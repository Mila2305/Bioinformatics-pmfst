"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement GreedySorting to Sort a Permutation by Reversals
Rosalind ID: BA6A
URL: http://rosalind.info/problems/ba6a/
"""

def GreedySorting(str_permutation):
    helper=[int(x) for x in str_permutation[1:-1].split()] #remove simbols "(" and ")"

    S=[]

    for i in range(0,len(helper)):
        if helper[i]==i+1: #skip if already in correct order 
            continue

        idx=i     #finding index of next correct element
        while True:
            if helper[idx]==i+1 or helper[idx]==-1*(i+1):
                break
            idx+=1

        mid=[-1*x for x in helper[i:(idx+1)]][::-1]

        helper=helper[0:i]+mid+helper[(idx+1):]

        S.append(helper.copy())

        if helper[i]<0:  #for reversal fliping
            helper[i]=abs(helper[i])
            S.append(helper.copy())

    if S==[]:
        S.append(helper)
    return S


def RosalindPrint(permutation):
    s=""
    for i in range(0,len(permutation)):
        s=s+"("
        for j in range(0,len(permutation[0])):
            if(permutation[i][j]>=0):
                s=s+"+" 
            s=s+str(permutation[i][j])+" "
        s=s[:-1]+") \n"
    return s[:-1]


x="""(-3 +4 +1 +5 -2)"""
#print(GreedySorting(x))
print(RosalindPrint(GreedySorting(x)))


