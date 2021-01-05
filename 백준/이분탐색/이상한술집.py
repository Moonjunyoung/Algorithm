def isPossible(ml):
    global makgulri,k
    cnt=0
    for i in makgulri:
        cnt+=i//ml ## 이진 탐색한 용량으로 막걸리를 몇개 나눌수있는지 확인

    if cnt>=k: #k명 이상에게 나눠줄수있으면
        return True
    else:
        return False

n,k=map(int,input().split())
makgulri=[]
for i in range(n):
    tmp=int(input())
    makgulri.append(tmp)


left=0 #막걸리의 최소 ml
right=max(makgulri) # 막걸리의 최대 ml

answer=0

while left<=right:
      mid=(left+right)//2
      if isPossible(mid):
          answer=max(mid,answer)
          left=mid+1 # 1. 더 큰 용량으로 탐색범위를 늘린다. (많이 커지게되면 막걸리를 분배할수없게됨)

      else:
          right=mid-1 # 2. 용량이 만족을 안하므로 탐색범위를 줄인다. (용량을 줄일수록 막걸리를 분배할수있는 양이 많아짐)


print(answer)