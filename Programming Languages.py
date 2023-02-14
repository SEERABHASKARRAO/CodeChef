# cook your dish here 
for _ in range(int(input())): 
    a,b,a1,b1,a2,b2=map(int,input().split()) 
    if((a==b1 or a==a1)and (b==b1 or b==a1)):
        print(1)
    elif((a==b2 or a==a2)and (b==b2 or b==a2)):
        print(2)
    else:
        print(0)
