
for _ in range(int(input())):
    n=int(input())
    s=input()
    a=s[:n//2]
    b=s[n//2:n]
    if(a==b or b==a):
        print("YES")
    else:
        print("NO")
