for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    b=[]
    for i in range(n-1):
        b.append(abs(l[i]-l[i+1]))
    print(min(b))
