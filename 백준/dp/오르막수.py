n=int(input())
dp=[0]*1001
for i in range(1,n+1):
    dp[i]=[0]*10

for i in range(10):
    dp[1][i]=1

# dp[n][0~9] n개의 길이 , 0~9로 시작하는수

for i in range(2,n+1):
    for j in range(10):
        for z in range(j,10):
            dp[i][j]+=dp[i-1][z]
            dp[i][j]%=10007

answer=sum(dp[n])
answer%=10007
print(answer)