def isPossible(splite_wire):
    global wire,n
    cnt=0
    for i in wire:
        cnt+=(i//splite_wire) #짜른랜선의 길이 몇개로 현재랜선값을 만들수있는지확인

    if cnt<n: ##짜른 랜선의길이로 n값을 만들수없으면
        return True

    return False


k,n=map(int,input().split())
wire=[]
for i in range(k):
    tmp=int(input())
    wire.append(tmp)

wire.sort()

answer=0
start=1
end=max(wire)
cur=0
while start<=end:
      mid=(start+end)//2 #랜선을 반으로 짜른다 (자른 랜선의길이로 n를 만들수있는지확인)

      if isPossible(mid):# 만들 수없으면
          end=mid-1 #랜선을 더 자른다.

      else: #만들수있으면 최대 랜선길이를 구해본다.
          start=mid+1
          answer=mid

print(answer)


