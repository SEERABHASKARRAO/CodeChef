# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    i=0
    while(i<n):
        if(i+1<n and s[i]==s[i+1] ):
            c+=1
            i+=2
        else:
            c+=1
            i+=1
    print(c)
