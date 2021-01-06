class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left=0
        right=len(height)-1

    # (right-left) =가로 * min을 해준이유는 물이넘치는것을 고려해야함
        answer=(right-left)*min(height[left],height[right])
        while left<=right:
            if height[left]<height[right]:
                left+=1

            else:
                right-=1


          #2. 물이 넘치는것을 고려
            answer=max(answer,(right-left)*min(height[left],height[right]))

        
        return answer