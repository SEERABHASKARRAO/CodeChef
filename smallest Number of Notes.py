# cook your dish here
for _ in range(int(input())):
    m=int(input())
    l=[1,2,5,10,50,100]
    l.sort(reverse=True)
    sum1=0
    p=0
    n=m
    c=0
    for i in l:
      if(n!=0 and n>=i):
        p=(n//i)
        sum1=sum1+(p*i)
        c=c+p
        n=m-sum1
      else:
          continue
    print(c)
