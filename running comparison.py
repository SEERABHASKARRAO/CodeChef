# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(a[i]<=(2*b[i]) and b[i]<=(2*a[i])):
            c+=1 
    print(c)
