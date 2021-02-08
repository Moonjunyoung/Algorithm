n=int(input())
m=int(input())
dp=[0]*41
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2] # 1. 좌석을 이동할수있는 경우의수 dp[3] = 3개의 좌석에서 나오는 경우의수 (피보나치와 동일)


cur=0
answer=1
for i in range(m):
    vip=int(input())
    answer*=dp[vip-cur-1] # 고정석 위치 - 현재위치 -1 = 고정석 이전의 좌석수
    cur=vip

answer*=dp[n-cur]
print(answer)