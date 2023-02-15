# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    a=10*x 
    if(a>=y):
        print(y*z)
    else:
        print(a*z)
