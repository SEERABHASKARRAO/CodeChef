
player1=0
player2=0
max1=0
max2=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    max1+=a
    max2+=b
    if(max1>max2):
        player1=max(player1,max1-max2)
    else:
        player2=max(player2,max2-max1)
if(player1>player2):
    print(1,player1)
else:
    print(2,player2)
