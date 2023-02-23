for _ in range(int(input())):
    x,y=map(int,input().split())
    s1=500-(x*2)
    s2=1000-((x+y)*4)
    r1=s1+s2
    t1=1000-(y*4)
    t2=500-((x+y)*2)
    r2=t1+t2
    print(max(r1,r2))
    
