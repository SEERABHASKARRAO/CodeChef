# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    s=input()
    p=[x]
    for i in s:
        if(i=='R'):
            p.append(p[-1]+1)
        else:
            p.append(p[-1]-1)
    print(len(set(p)))
