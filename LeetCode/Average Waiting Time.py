import heapq
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time=0
        answer=0

        # customer의 시작시간이상이여야함
        for customer in customers:
            wait_time=max(wait_time,customer[0])
            wait_time+=customer[1]
            answer+=wait_time-customer[0]


        return answer / len(customers)


