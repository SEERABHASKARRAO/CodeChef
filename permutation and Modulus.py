# cook your dish here
for _ in range(int(input())):
    n=int(input())
    p=[]
    for i in range(1,n+1):
        p.append(i)
    for i in range(n-1):
        p[i],p[i+1]=p[i+1],p[i]
    print(*p)
    
