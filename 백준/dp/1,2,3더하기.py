n=int(input())

dp=[0]*12
dp[1]=1
dp[2]=2
dp[3]=4

while n!=0:
      number=int(input())
      for i in range(4,number+1):
          dp[i]=dp[i-1]+dp[i-2]+dp[i-3]


      print(dp[number])
      n-=1