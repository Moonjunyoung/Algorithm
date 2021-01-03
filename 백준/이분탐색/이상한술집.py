def isPossible(value):
    global k,drink
    cnt=0
    for i in drink: # 쪼갠값 으로 k이상이 되는지 확인함
        cnt+=i//value

    if cnt>=k: 
        return True

    return False
n,k=map(int,input().split())
drink=[]
for i in range(n):
    tmp=int(input())
    drink.append(tmp)


drink.sort()
start=0
end=max(drink)
answer=0
while start<=end:
      mid=(start+end)//2
      if isPossible(mid):
          answer=max(answer,mid)
          start=mid+1
      else:
          end=mid-1

print(answer)