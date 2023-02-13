# cook your dish here
for _ in range(int(input())):
    a,b,c,d,n=map(int,input().split())
    x=c*n
    y=d*n
    if(b-a>=x and b-a<=y):
        print(1)
    else:
        print(0)
