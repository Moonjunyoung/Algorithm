h,w=map(int,input().split())
block_list=list(map(int,input().split()))


answer=0
for i in range(1,len(block_list)):
    left=i-1
    right=i+1
    block_height=block_list[i]

    left_max_height=block_height
    # 1. 현재 위치에서 왼쪽에있는 높이들중 가장큰 높이를 구함
    while left>=0:
          if left_max_height<block_list[left]:
              left_max_height=block_list[left]

          left-=1


    right_max_height=block_height
    # 2. 현재 위치에서 오른쪽에있는 높이들 중 가장 큰 높이를 구함
    while right<len(block_list):
          if right_max_height<block_list[right]:
             right_max_height=block_list[right]

          right+=1

    # 3. 왼쪽 오른쪽 가장 큰 높이 중 작은것으로 선정
    tmp=min(left_max_height,right_max_height)

    if tmp>block_height:
        # 4. 선정된 높이 - 현재 블록높이 =빗물을 채울수있는칸의수  
       answer+=tmp-block_height


print(answer)