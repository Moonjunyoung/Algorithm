import sys

n,m=map(int,sys.stdin.readline().split())
number_list=map(int,sys.stdin.readline().split())
dp=[0]*(n+1) # 1~n 까지누적합
s=0
idx=1
for i in number_list:
    s+=i
    dp[idx]=s
    idx+=1

while m!=0:
      start,end=map(int,sys.stdin.readline().split())
      answer=dp[end]-dp[start-1]
      print(answer)
      m-=1