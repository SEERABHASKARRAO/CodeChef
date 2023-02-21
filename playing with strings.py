from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=input()
    r=input()
    s=list(s)
    r=list(r)
    t1=[]
    t2=[]
    t1.append(s.count('0'))
    t1.append(s.count('1'))
    t2.append(r.count('0'))
    t2.append(r.count('1'))
    if(t1==t2):
        print("YES")
    else:
        print("NO")
