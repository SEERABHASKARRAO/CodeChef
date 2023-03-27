# cook your dish here
for _ in range(int(input())):
    x=int(input())
    c=0
    if(x%5!=0):
        print(-1)
    else:
        while(x%10!=0):
            x=x*2
            c+=1
        print(c)
