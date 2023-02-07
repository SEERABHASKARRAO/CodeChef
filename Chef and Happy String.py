# cook your dish here
for _ in range(int(input())):
    s=input()
    if all(i in 'aeiou' for i in s):
        if(len(s)>2):
         print("Happy")
    else:
        n=0
        for i in s:
            if i  in 'aeiou':
                n+=1 
            elif(n>2):
                break
            else:
                n=0
        if(n>2):
            print("Happy")
        else:
            print("Sad")
            
