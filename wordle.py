for _ in range(int(input())):
    s=input()
    t=input()
    res=''
    for i in range(len(s)):
        if s[i]==t[i]:
            res+='G'
        else:
            res+='B'
    print(res)
