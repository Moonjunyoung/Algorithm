n=int(input())
wires=[]
max_wire=0
for i in range(n):
    a,b=map(int,input().split())
    wires.append([a,b])
    max_wire=max(max_wire,b)

wires=sorted(wires,key= lambda x:x[0])
dp=[0]*(max_wire+1)
for i in range(n):
    cur_wire=wires[i][1]
    dp[cur_wire]=1
    # 가장 긴 부분증가수열 (LIS) = 교차되지않은 전기줄의수
    for j in range(i):
        target_wire=wires[j][1]
        if cur_wire> target_wire and dp[cur_wire]<dp[target_wire]+1:
            dp[cur_wire]=dp[target_wire]+1


# 전체전깃줄 - 교차되지않은 전기줄수 = 교차된 전기줄의수
print(n-max(dp))