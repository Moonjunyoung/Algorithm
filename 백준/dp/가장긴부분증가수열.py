n=int(input())
number_list=list(map(int,input().split()))
dp=[0]*n
for i in range(len(number_list)):
    dp[i]=1
    for j in range(i):
        if number_list[i]>number_list[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1



# 1. 현재 숫자의 왼쪽에있는것들중 작은 것들만 후보가 가능

print(max(dp))



