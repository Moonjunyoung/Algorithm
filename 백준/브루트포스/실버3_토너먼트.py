n,a,b=map(int,input().split())

round=1
while n:
    if ((a+1)//2)==((b+1)//2): ##라운드올라갈떄마다 +1 //2를하게됨
        break

    else:
        a=(a+1)//2
        b=(b+1)//2
        n=n//2
        round+=1


if n==0:
    print(-1)
    exit(0)

else:
    print(round)
