for _ in range(int(input())):
    s=input()
    s=list(s)
    sum1=0
    t=[]
    for i in s:
        if(ord(i)>=48 and ord(i)<=57):
            sum1+=int(i)
    print(sum1)
