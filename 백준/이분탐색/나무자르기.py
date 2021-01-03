n,m=map(int,input().split())
trees=list(map(int,input().split()))
trees.sort()

start=0
end=max(trees)
answer=0
while start<=end:
      mid=(start+end)//2 # 절단기 높이
      total=0
      for i in trees:
          if i<=mid:continue
          else:
              total+=i-mid

      if total>=m: # 절단한 값들이 m보다 큰경우 범위를 축소시킴
          answer=max(answer,mid)
          start=mid+1
      else: #m이상인경우
          end=mid-1




print(answer)