n=int(input())
tmp_list=list(map(int,input().split()))
cards=[0]*(n+1)
dp=[0]*(n+1)

for i in range(1,n+1):
    cards[i]=tmp_list[i-1]

dp[1]=cards[1]
for i in range(2,n+1):
    dp[i]=cards[i]
    for j in range(1,i+1):
        dp[i]=min(dp[i],dp[i-j]+cards[j]) 
        # i 개 카드를 사는데 최소비용  


print(dp[n])

