# feb contest 08-02-2023
for _ in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        l.sort(reverse=True)
        maxi=0
        c=0
        for i in l:
            if(i>=maxi):
                maxi=i
                c+=1
            if(c%2==0 and c>=2 and c<n):
                maxi=l[c]
        if(c%2==0):
            print("zenyk")
        else:
            print("marichka")
        
