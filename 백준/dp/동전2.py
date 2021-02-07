n,k=map(int,input().split())
coin_list=[]
dp=[10001]*(k+1)
dp[0]=0
for i in range(n):
    coin_list.append(int(input()))

coin_list.sort()



for i in range(n):
    for j in range(coin_list[i],k+1):
        dp[j]=min(dp[j],dp[j-coin_list[i]]+1)


if dp[k]==10001:
    print(-1)
else:
    print(dp[k])