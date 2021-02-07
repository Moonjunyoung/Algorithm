n=int(input())
cows={}
cnt=0
for i in range(n):
    number,pos=map(int,input().split())
    if number not in cows:
        cows[number]=pos
    else:
        if cows[number]!=pos:
            cows[number]=pos
            cnt+=1


print(cnt)  