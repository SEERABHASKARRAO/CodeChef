# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    res=a+(a*(d/100))
    if(res>=b and res<=c):
        print("Yes")
    else:
        print("No")
