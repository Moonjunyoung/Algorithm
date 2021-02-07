n,k=map(int,input().split())

dp=[0]*(k+1)
dp[0]=1
#  dp [i] = 해당숫자를 만들수있는 경우의수
#  1로만 만들경우 1 ~10 전부다 1
#  1과 2로 만들경우 1 =1 , 2= 1+1 ,2 2개   , 3 =(1+2) ,(1+1+1) 2개

for i in range(n):
    number=int(input())
    for i in range(number,k+1):
        dp[i]=dp[i]+dp[i-number] # 기존의 경우의수 + 새로운수를 추가한거에대한  경우의수

print(dp[k])