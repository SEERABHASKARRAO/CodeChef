# cook your dish here
for _ in range(int(input())):
    n,k,v=map(int,input().split())
    l=list(map(int,input().split()))
    p=sum(l)
    y=v*(n+k)
    r=y-p
    if(r%k==0 and r>0):
        print(r//k)
    else:
        print(-1)
