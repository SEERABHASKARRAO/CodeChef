# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    cy=a+b
    ct=str(cy)
    c=0
    for i in ct:
        if(i=='1'):
            c+=2
        elif(i=='2' or i=='3' or i=='5'):
            c+=5
        elif(i=='4'):
            c+=4
        elif(i=='6' or i=='9' or i=='0'):
            c+=6
        elif(i=='8'):
            c+=7
        else:
            c+=3
    print(c)
