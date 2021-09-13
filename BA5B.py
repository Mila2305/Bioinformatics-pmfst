"""
A solution to a Rosalind bioinformatics problem
Problem Title: Find the Length of a Longest Path in a Manhattan-like Grid
Rosalind ID: BA5B
URL: http://rosalind.info/problems/ba5b/
"""


def manhattantourist(n, m, down, right):
    s = []
    for i in range(0,n + 1):
        s.append( [0]*(m + 1) )

    #for first column
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    #for first row
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    #for all other
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]

x="""4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2"""
inlines=x.split("\n")
n,m=inlines[0].split()
n=int(n)
m=int(m)
down=[]
for i in range(1,n+1):
    down.append([int(x) for x in inlines[i].split()])
right=[]
for i in range(0,n+1):
    right.append([int(x) for x in inlines[n+2+i].split()])
print(manhattantourist(n,m,down,right))
