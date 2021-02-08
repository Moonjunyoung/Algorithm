n=int(input())
grape_juice=[0]*(n+1)
dp=[0]*(n+1)
for i in range(1,n+1):
    grape_juice[i]=int(input())


dp[1]=grape_juice[1]
if n>=2:
   dp[2]=grape_juice[1]+grape_juice[2]

# 포도주를 연속 두번 먹음 = dp[i-3]+grape_juice[i-1]+grape_juice[i+1]
# 포도주를 연속 한번 먹음 = dp[i-2]+grape_juice[i]
# 현재 포도주를 안먹음 = dp[i-1]
for i in range(3,n+1):
    dp[i]=dp[i-2]+grape_juice[i]
    dp[i]=max(dp[i],dp[i-3]+grape_juice[i-1]+grape_juice[i])
    dp[i]=max(dp[i-1],dp[i])

print(max(dp))