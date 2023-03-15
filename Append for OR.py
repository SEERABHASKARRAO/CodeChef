for _ in range(int(input())):
        n,y=map(int,input().split())
        l=list(map(int,input().split()))
        res=l[0]
        for i in range(1,len(l)):
            res=res|l[i]
        if(res==y):
            print(0)
        else:
            t=y-res
            if(res|t==y):
                print(t)
            else:
                print(-1)
          
