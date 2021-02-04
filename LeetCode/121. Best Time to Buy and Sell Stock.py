from typing import List



# 1. 가격 리스트들중에 최대이익을 얻을수있는 경우를 구하면된다 .
# 2. 이떄 현재가격의 왼쪽에있는 것들만 뺼수있다 
# 3. 현재 가격에서 왼쪽에있는것들중 가장 작은값을 찾고  현재가격에서 뺀것중 가장 큰 값을 구하면된다.
# 이게왜 디피지?

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        answer=0

        min_value=2100000000

        for i in prices:
            min_value=min(min_value,i) # 가장 작은값을구함
            answer=max(answer,i-min_value)




        return answer
