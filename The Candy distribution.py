for _ in range(int(input())):
    n,m=map(int,input().split())
    flag=1
    if((n%m)==0):
        if((int(n/m))%2==0):
            flag=0
        else:
            flag=1
    if(flag==0):
        print("Yes")
    else:
        print("No")
