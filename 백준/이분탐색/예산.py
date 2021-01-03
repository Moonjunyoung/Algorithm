n=int(input())
money=list(map(int,input().split()))
money.sort()
max_money=int(input())

start=0 ##
end=max(money)
answer=0
# 1. 상한액을 중간값으로 잡고 total값이 예산보다 크면 시작값을 mid+1로 두고 탐색 
while start<=end:
      mid=(start+end)//2
      total=0
      for x in money:
          if x<mid: # 상한액보다 작으면
              total+=x
          else:
              total+=mid

      if total>max_money: # 답을 못찾는경우
          end=mid-1
      else:
          answer=mid
          start=mid+1

print(answer)