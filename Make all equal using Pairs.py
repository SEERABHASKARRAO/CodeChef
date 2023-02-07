from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
   
    print(n-max(Counter(l).values()))
