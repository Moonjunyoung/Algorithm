n=int(input())
number_list=[]
dp=[0]*n
while n!=0:
      tmp=int(input())
      number_list.append(tmp)
      n-=1

for i in range(len(number_list)):
    dp[i]=1
    for j in range(i):
        if number_list[i]>number_list[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1

#  가장긴 부분증가 수열을 구함 (이부분은 냅두고 나머지 사람들을 바꿔주기만하면 줄세우는경우를 구할수있음)
#  전체길이에서 - 가장긴부분증가수열 하면 =줄세우는경우


print(len(number_list)-max(dp))
