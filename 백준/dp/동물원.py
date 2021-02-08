n=int(input())
dp=[0]*(n+1)
for i in range(n+1):dp[i]=[0]*3

dp[1][0]=1 # 왼쪽배치
dp[1][1]=1 # 오른쪽배치
dp[1][2]=1 # 배치 x

for i in range(2,n+1):
    dp[i][0]=dp[i-1][2]+dp[i-1][1] # 1. 현재 왼쪽에 배치하면 이전칸의 오른쪽과 배치x 경우가 옴
    dp[i][1]=dp[i-1][0]+dp[i-1][2] # 2. 현재 오른쪽배치 하면 이전칸의 왼쪽과 배치x 경우가 옴
    dp[i][2]=dp[i-1][2]+dp[i-1][1]+dp[i-1][0] # 현재 배치 x 세가지경우가 다옴
    dp[i][0] %= 9901
    dp[i][1] %= 9901
    dp[i][2] %= 9901

answer=dp[n][0]+dp[n][1]+dp[n][2]
answer%=9901
print(answer)

