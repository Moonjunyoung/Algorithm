n=int(input())
dp=[0]*1001

dp[1]=1 # 상근
dp[2]=0 # 상근->창영
dp[3]=1 # 상근 -> 창영 -> 상근 # 돌이 3개부터시작해도 상근 승
dp[4]=1 # 돌이 4개 부터 시작하면 상근승

# 돌이 5개일떄 3개 상근 2개 창영 창영승 , 돌4개 상근 돌1개 창영 창영승
for i in range(5,n+1):
    if min(dp[i-4],min(dp[i-3],dp[i-1]))==0:
        dp[i]=1
    else:
        dp[i]=0


if dp[n]==1:
    print('SK')
else:
    print('CY')


