for _ in range(int(input())):
    a,b=map(int,input().split())
    res=a+((7/100)*a)
    if(b<=res):
        print("YES")
    else:
        print("NO")
