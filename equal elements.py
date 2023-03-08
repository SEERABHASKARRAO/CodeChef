from collections import Counter 
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if(len(a)==len(set(a))):
        print(len(a)-1)
    else:
     print(len(a)-max(Counter(a).values()))
