# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(len(l)):
        if(l[i]%2!=0):
            c+=1
    if(c>0 and c%2==0):
        print("YES")
    else:
        print("NO")
