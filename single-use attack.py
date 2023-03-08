import math
for _ in range(int(input())):
    h,x,y=map(int,input().split())
    c=1
    h=h-y
    print(c+(math.ceil(h/x)))
