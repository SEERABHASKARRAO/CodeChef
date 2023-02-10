from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    # if(len(set(l))==1):
    #     print(0)
    # elif(len(l)==2):
    #     print(1)
    # else:
    p=max(Counter(l).values())
    print(n-p)
