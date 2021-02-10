n=int(input())

jump_list=[0]*(n+1)
tmp_list=list(map(int,input().split()))
for i in range(1,n+1):
    jump_list[i]=tmp_list[i-1]
dp=[9999]*(n+1)
dp[1]=0

for i in range(2,n+1):
    for j in range(i-1,0,-1):
        # 1. 현재위치의 이전것들중에 현재위치로 점프할수있는것중 가장 최소값을 구함
        if jump_list[j]+j>=i:
            dp[i]=min(dp[i],dp[j]+1)


if dp[n]==9999:
    print(-1)
else:
    print(dp[n])