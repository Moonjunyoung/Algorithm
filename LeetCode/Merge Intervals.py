from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer=[]
        start=intervals[0]

        for interval in intervals:
            if interval[0]>start[1]: #1. 해당 interval의 시작하는부분이  현재 끝나는 구간보다 클경우
                # 2. 새로운 구간 시작
                answer.append(start)
                start=interval

            elif interval[0]<=start[1]: # 2.해당 interval 시작하는부분이 현재 끝나는 구간보다 작을경우 (겹치는구간)
                 # 2-1 해당 interval의 끝나는 구간이 더작을수있으므로  현재끝나는구간과비교후 끝나는구간정함
                 start[1]=max(start[1],interval[1])


        answer.append(start)
        return answer


a=Solution()
#a.merge([[1,3],[2,6],[8,10],[15,18]])
a.merge([[1,4],[2,3]])