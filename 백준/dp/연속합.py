n=int(input())
number_list=list(map(int,input().split()))
dp=[-10000]*(n+1)

dp[0]=number_list[0]

for i in range(1,n):
    dp[i]=number_list[i]
    # 1. 이전까지의  최대연속 합과 현재값을 더했을떄 현재값보다 작은경우 갱신 
    if dp[i-1]+number_list[i]<dp[i]:
        dp[i]=number_list[i]
    
    # 2. 현재값보다 큰경우는 다시 연속합 갱신
    else:
        dp[i]=dp[i-1]+number_list[i]


print(max(dp))