# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    b=[]
    for i in l:
         c=0
         for j in l:
             if(i<j):
                 c+=1
         b.append(c)
    print(*b)
                 
