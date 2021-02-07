n=int(input())
stair_list=[0]*301
dp=[0]*301
for i in range(n):
    tmp = int(input())
    stair_list[i]=tmp


dp[0]=stair_list[0]
dp[1]=stair_list[0]+stair_list[1]
dp[2]=max(stair_list[0]+stair_list[2],stair_list[1]+stair_list[2])

for i in range(3,len(stair_list)):
    dp[i]=dp[i-2]+stair_list[i] # 이전이전 계단에서 현재 계단으로 올라오는경우 
    dp[i]=max(dp[i-3]+stair_list[i-1]+stair_list[i],dp[i])
    ## 이전이전

print(dp[n-1])
