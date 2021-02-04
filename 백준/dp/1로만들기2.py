n=int(input())
dp=[0 for _ in range(n+1)]
answer=[0 for _ in range(n+1)]

dp[1]=0
answer[1]=-1
for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    answer[i]=i-1

    if i%2==0 and dp[i]>dp[i//2]+1: # 2로나누어떨어지면
       dp[i]=min(dp[i],dp[i//2]+1)
       answer[i]=i//2

    if i%3==0 and dp[i]>dp[i//3]+1: # 3으로 나누어떨어지면
       dp[i]=min(dp[i],dp[i//3]+1)
       answer[i]=i//3




print(dp[n])

while n!=-1:
      print(n,end=' ')
      n=answer[n]



