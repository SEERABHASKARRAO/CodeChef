# cook your dish here
n=int(input())
l=list(map(int,input().split()))
odd=0
even=0
for i in l:
    if i%2==0:
        even+=1 
    else:
        odd+=1 
if(even>odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
