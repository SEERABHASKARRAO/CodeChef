for _ in range(int(input())):
    n=int(input())
    s=input()
    a=[999]*n
    for i in range(n):
      if(i<len(s)):
        if(s[i]=='0'):
            a[i]=a[i]-1
        else:
            a[i+1]=a[i]-1 
    a.sort(reverse=True)
    print(a.count(a[0]))
