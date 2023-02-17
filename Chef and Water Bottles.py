
for _ in range(int(input())):
    n,x,k=map(int,input().split())
    if((k//x)<=n):
        print(k//x)
    else:
        print(n)
