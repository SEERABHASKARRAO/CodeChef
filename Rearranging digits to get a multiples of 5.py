# cook your dish here
for _ in range(int(input())):
    n=int(input())
    m=input()
    if(int(m)%5==0):
        print("YES")
    else:
        if('0' in m or '5' in m):
            print("YES")
        else:
            print("NO")
