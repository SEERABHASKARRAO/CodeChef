# cook your dish here
for _ in range(int(input())):
    p=int(input())
    a=[0]*12
    for i in range(len(a)):
        a[i]=2**i 
    a.sort(reverse=True)
    c=0
    sm=0
    n=p
    for i in a:
        if(p>=0 and p>=i):
            t=p//i
            sm+=(t*i)
            c+=t
            p=n-sm
            
    print(c)
