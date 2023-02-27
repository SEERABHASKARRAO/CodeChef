# cook your dish here
for _ in range(int(input())):
    n=int(input())
    p=[0]*10
    for i in range(n):
        t=input()
        for j in range(len(t)):
            p[j]=p[j]^int(t[j])
    print(p.count(1))
    
