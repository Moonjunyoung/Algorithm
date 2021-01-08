import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = []

        # 1. target의 왼쪽에 삽입할수있는 위치를 찾는다.
        left = bisect.bisect_left(nums, target)

        # 2. target의 오른쪽에 삽입할수있는 위치를 찾는다
        right = bisect.bisect_right(nums, target)

        # 3. 2 이상이면 원소가 두개이상 있다는것
        if right - left >= 2:
            answer.append(left)
            answer.append(right - 1)

        #  1이상이면 원소가 한개
        elif right - left == 1:
            answer.append(left)
            answer.append(left)

        # 아예없다는것
        else:
            answer.append(-1)
            answer.append(-1)

        return answer
