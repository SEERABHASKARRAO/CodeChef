# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
          x,y=map(int,input().split())
          a.append(x)
          b.append(y)
    c=[0]*9
    for i in range(n):
      if(a[i]>=1 and a[i]<=8):
        if(c[a[i]]<=b[i]):
            c[a[i]]=b[i]
    print(sum(c))    
