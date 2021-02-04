n=int(input())
number_list=list(map(int,input().split()))
dp=[0]*n
for i in range(len(number_list)):
    dp[i]=number_list[i]
    for j in range(i):
        if number_list[i]>number_list[j] and dp[i]<dp[j]+number_list[i]:
            dp[i]=dp[j]+number_list[i]

# 1. 현재 숫자의 왼쪽에있는것들중 작은 것들만 후보가 가능
# dp [i] = 해당 i 까지의 가장 큰 부분 증가수열

print(max(dp))



