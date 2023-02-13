t=int(input())
for i in range(t):
    N,S=map(int,input().split())
    Sum=S-N
    if(N<S and S!=0):
        print(N-Sum)
    elif(N>S and N!=0):
        print(S)
    else:
        print(N)
