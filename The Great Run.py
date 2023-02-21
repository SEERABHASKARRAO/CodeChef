for _ in range(int(input())):
    n,a=map(int,input().split())
    l=list(map(int,input().split()))
    maxi=-99999
    for i in range(n-1):
        sum1=sum(l[i:i+a])
        maxi=max(maxi,sum1)
    print(maxi)
    
