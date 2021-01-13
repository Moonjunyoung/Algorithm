class Solution:
    def isPossible(self,distance,position,m):
        cnt=1
        prev=0
        for i in range(len(position)):
            if i==0:
                prev=position[i]
            else:
                if distance<=position[i]-prev:
                   cnt+=1
                   prev=position[i]

        if cnt>=m:
            return True

        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        left=1
        right=max(position)
        position.sort()
        answer=0
        while left<=right:
              mid=(left+right)//2
              if self.isPossible(mid,position,m):
                  left=mid+1
                  answer=mid
              else:
                  right=mid-1



        return answer