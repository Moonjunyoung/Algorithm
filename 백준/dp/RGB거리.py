n=int(input())
board=[0]*n
dp=[0]*n
for i in range(n):
    board[i]=list(map(int,input().split()))
    dp[i]=[0]*n



# 0 빨간색 1 파란색 2 초록색
dp[0][0]=board[0][0]
dp[0][1]=board[0][1]
dp[0][2]=board[0][2]

# dp [고를집][색깔]의 최소값
# 빨간색을 고를경우 -> 이전값은 같은값을 못고르므로 파란색 or 초록색이 올수밖에없음
# 파란색 -> 이전값은 같은값을 못고르므로 빨간 or 초록

for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+board[i][0]
    dp[i][1]=min(dp[i-1][2],dp[i-1][0])+board[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+board[i][2]


print(min(dp[n-1][0],min(dp[n-1][1],dp[n-1][2])))
