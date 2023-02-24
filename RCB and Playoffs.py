for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if(x+(z*2)>=y or x+(z*1)>=y):
        print("YES")
    else:
        print("NO")
