
for _ in range(int(input())):
    n=int(input())
    c=0
    for i in range(1,n+1):
        i=i*(i+1)/2
        if(i>n):
            break
        else:
            c+=1 
    print(c)
