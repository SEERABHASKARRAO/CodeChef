# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    print((2*(x-1))+min(y-1,z-1)+min(y-1,x-z)+min(x-y,z-1)+min(x-y,x-z))

    
