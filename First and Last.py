# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    for i in range(len(a)):
        m=m if m>a[i]+a[i-1] else a[i]+a[i-1]
    print(m)
    
