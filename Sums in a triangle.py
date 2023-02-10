# cook your dish here
for _ in range(int(input())):
    n=int(input())
    i=0
    j=0
    v=[[0 for j in range(i+1)]for i in range(n)]
    l=[]
    for i in range(n):
        a=list(map(int,input().split()))
        l.append(a)
    
    
    
    for i in range(len(l)-2,-1,-1):
        for j in range(len(l[i])):
            l[i][j]+=max(l[i+1][j],l[i+1][j+1])
    print(l[0][0])
