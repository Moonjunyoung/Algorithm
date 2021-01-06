def binary_search(li,h): # 높이 h에 대하여 부딪힐수있는개수를 센다
    # 부딪힐수있는개수 = 높이 h와 겹치는것들 (높이 h보다 크거나같은것들)

    left=0
    right=len(li)-1
    mid=0
    while left<=right:
          mid=(left+right)//2
          if li[mid]>=h: #
              right=mid-1

          else:
              left=mid+1

    # 리스트 길이 -높이 h의 왼쪽에 삽입될 인덱스 = 충돌가능한것들
    return len(li)-left

n,h=map(int,input().split())
bottom=[]
top=[]
for i in range(1,n+1):
    tmp=int(input())
    if i%2==0: ##종유석
        top.append(tmp)
    else: # 석순
        bottom.append(tmp)

bottom.sort()
top.sort()
answer=999999999
cnt=0
for height in range(1,h+1): # 높이 hegiht에 대하여 이분탐색
    bottom_crash_cnt=binary_search(bottom,height)
    top_crash_cnt=binary_search(top,(h-height)+1)
    # h-height를 해주는 이유는 높이가 1인것을 통과할떄는 바닥기준으로 높이가 1이상인것들은 충돌가능하다
    # 그러나 높이가 1이므로 종유석의 길이는 5이상이되어야 충돌이가능하므로


    if bottom_crash_cnt+top_crash_cnt<answer:
       answer=bottom_crash_cnt+top_crash_cnt
       cnt=1

    elif bottom_crash_cnt+top_crash_cnt==answer:
         cnt+=1


print(answer,cnt)