n=int(input())
dp=[0]*1001
for i in range(1,n+1):
    dp[i]=[0]*10

for i in range(1,10):
    dp[1][i]=1


# 길이가 n이고 첫숫자가 n으로 시작하는 것
# 길이가 2이고 첫숫자가 1일떄 dp[2][1] = dp[1][0] , dp[1][2]
for i in range(2,n+1):
    for j in range(10):
        if j-1>=0:  
           dp[i][j]+=dp[i-1][j-1]

        if j+1<10:
            dp[i][j]+=dp[i-1][j+1]

        dp[i][j]%=1000000000

answer=sum(dp[n])
answer%=1000000000
print(answer)

