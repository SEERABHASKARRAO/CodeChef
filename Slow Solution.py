# cook your dish here
for _ in range(int(input())):
    t,n,sumn=map(int,input().split())
    sum1=n
    sum2=0
    maxi=0
    k=sumn//n
    for i in range(t):
        if(sum1<=sumn):
            sum2+=(n*n)
            maxi=sum2
            sum1+=n
        else:
            if((sumn-(k*n))>0):
             maxi+=(sumn-(k*n))**2
            break 
    print(maxi)
