# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(len(l)==1 or len(set(l))==1 or len(set(l))==len(l)):
        print(len(set(l)))
    else:
        i=1
        c=0
        while(i<len(l)-1):
            if(l[i]==l[i+1] or l[i]==l[i-1]):
                c+=1
                l.pop(i)
                i=1
            else:
                i+=1
        print(n-c)
    
