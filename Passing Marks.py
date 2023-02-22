# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    p=l[0:x]
    print(p[-1]-1)
