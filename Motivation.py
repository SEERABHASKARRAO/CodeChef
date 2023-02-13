import operator
for _ in range(int(input())):
    n,x=map(int,input().split())
    s=[]
    for i in range(n):
        a,b=map(int,input().split())
        s.append([a,b])
    s.sort(reverse=True,key=operator.itemgetter(1))
    maxi=0
    for i in range(len(s)):
        if(s[i][0]<=x):
            maxi=max(maxi,s[i][1])
    print(maxi)
