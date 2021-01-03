# 다시 풀기 나중에 
def isPossible(mid):
    global money,n,m
    sum=mid
    k=1
    for i in money:
        if mid<i: #현재금액을 인출이 불가능한경우
            return False

        if sum-i<0:
           sum=mid ##돈이 모자라게되면 k원을 인출한다.
           k+=1

        sum-=i



    return k<=m ## m을 넘기지 않아야 True

n,m=map(int,input().split())
money=[]
s=0
for i in range(n):
    tmp=int(input())
    money.append(tmp)
    s+=tmp

start=1
end=s ##최대 나올수있는 돈
answer=987654321
while start<=end:
      mid=(start+end)//2
      if isPossible(mid): ## 이조건은 m을 넘어가지 않아야 성립함 
          answer=min(answer,mid)
          end=mid-1
      else: ##인출금액이 적은경우 더 큰 금액에서 탐색
          start=mid+1

print(answer)