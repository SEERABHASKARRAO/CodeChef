for _ in range(int(input())):
        a,b,c=map(int,input().split())
        t=min(b,c)
        b=b-t
        c=c-t
        t=min(a,c)
        a=a-t
        c=c-t
        t=min(a,b)
        a=a-t
        b=b-t
        if(a>0): 
            print("YES")
        else:
            print("NO")
