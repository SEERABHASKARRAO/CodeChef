#08-02-2022 contest
# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=input().lower()
    s=list(s)
    if(len(set(s))==len(s)):
        print(-1)
    elif(len(set(s))==1):
        if(len(s)>=3):
          print(len(s)-2)
        else:
            print(0)
    else:
        t=max(Counter(s).values())
        if(t>=2):
            print(len(s)-2)
        else:
            print(-1)
        
