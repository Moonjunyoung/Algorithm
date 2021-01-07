n=int(input())
water_list=list(map(int,input().split()))
left=0
right=len(water_list)-1
water_list.sort()
answer_list=[0,0]
answer=2000000000


# 1. left 는 제일 작은값을 가리키고있음, right 는 제일 큰 값을 가리키고있음
while left<right:
      # 2. 0에 가까운 경우 answer를 갱신시킴 (즉 작을수록)
      if abs(water_list[left]+water_list[right])<answer:
         answer_list[0]=water_list[left]
         answer_list[1]=water_list[right]
         answer=abs(water_list[left]+water_list[right])


      # 3. 두 포인터의 합이 0 보다 작은경우 = 즉 left를 만족시키는경우 left는 더이상 볼필요 x
      if water_list[left]+water_list[right]<0:
          left+=1

      # 3-2 . 두 포인터의 합이 0보다 큰경우 = 즉 right를 만족시키므로 더이상 right는 볼필요 x
      else:
          right-=1

print(answer_list[0],answer_list[1],end=' ')