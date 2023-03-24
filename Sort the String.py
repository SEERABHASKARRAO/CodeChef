
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    for i in range(1,len(s)):
        if(s[i]=='0' and s[i-1]=='1'):
            c+=1 
    print(c)
