class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        answer=0

        left=0
        right=0
        dic={}
        s=0
        while right<len(nums):
              if nums[right] not in dic: # 1. 현재구간내에 중복된값이 없으면
                  dic[nums[right]]=1
                  s+=nums[right] # 답 갱신
                  answer = max(s, answer)
                  right += 1
              else:
                  while nums[right] in dic: # 2. 현재구간내에 중복된값이 존재하면
                        s-=nums[left] # 중복된값이 없어지는 구간이 나올떄까지 left를 증가한다
                        del dic[nums[left]]
                        left+=1


        return answer
