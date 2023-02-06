# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    c=0
    t=0
    for i in range(n):
        if(l[i]=='START38'):
            c+=1
        else:
            t+=1
    print(c,t)
