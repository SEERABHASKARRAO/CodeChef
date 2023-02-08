# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=max(Counter(l).values())
    print(n-m)
    
