# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    if(m==0):
        print(n*2)
    elif(n>m):
        print(n*2-m)
    else:
        print(n)
