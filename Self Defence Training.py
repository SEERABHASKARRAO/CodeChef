# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if(i>=10 and i<=60):
            c+=1 
    print(c)
