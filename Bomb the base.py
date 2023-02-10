# cook your dish here
for  _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    maxi=n-1
    l.reverse()
    for i in range(len(l)):
        if(l[i]<x):
            c=0
            maxi=i+1
            break
        else:
         c=1
    if(c==1):
        print(0)
    else:
     print(n-maxi+1)
    
            
