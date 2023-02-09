# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    sum=0
    i=0
    while(i<a):
        sum+=b
        i+=1 
        if(i%3==0 and i!=a):
            sum+=c
    print(sum)
