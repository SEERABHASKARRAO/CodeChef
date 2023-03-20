t=int(input())
while t!=0:
    n=int(input())
    s=input()
    l=[]
    for i in s:
        if i=='H' or i=='T':
            l.append(i)
    l=''.join(l)
    if len(l)==0:
        print("Valid")
    else:
        k=l.count('HT')
        if len(l)%2==0:
            if k==len(l)//2:
                print("Valid")
            else:
                print("Invalid")
        else:
            if k==len(l)//2+1:
                print("Valid")
            else:
                print("Invalid")
 
    t-=1
           
