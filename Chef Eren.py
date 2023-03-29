# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    e=[]
    o=[]
    for i in range(1,n+1):
        if(i%2==0):
            e.append(i)
        else:
            o.append(i)
    print(len(e)*a+len(o)*b)
