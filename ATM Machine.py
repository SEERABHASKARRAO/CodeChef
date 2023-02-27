for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    p=''
    sum1=0
    for i in l:
        if(i<=k):
            k-=i
            p+='1'
        else:
            p+='0'
    print(p)
    
