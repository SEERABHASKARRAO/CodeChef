for _ in range(int(input())):
    a,b=map(int,input().split())
    c=0
    
    for i in range(a,b+1):
        i=str(i)
        if(i[-1]=='2' or i[-1]=='3' or i[-1]=='9'):
            c+=1 
    print(c)
