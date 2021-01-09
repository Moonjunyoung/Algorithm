nums=[2,0,2,1,1,0]


for i in range(len(nums)):
    right=len(nums)
    idx=i
    # 1. idx = i (즉 현재위치로 잡는다)
    left = i + 1

    # 2. left < right를 돌면서 현재위치보다 작은값을 찾고 저장을 시켜놓는다
    while left<right:
          if nums[idx]>nums[left]:
             idx=left

          left+=1

    # 3. 저장시켜놓은 위치와 스왑한다. 
    tmp=nums[i]
    nums[i]=nums[idx]
    nums[idx]=tmp


print(nums)




