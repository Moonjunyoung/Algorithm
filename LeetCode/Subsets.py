from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer_list=[]
        def dfs(number_list,idx):
            if len(number_list) > len(nums):
                return
            else:
                if len(number_list) == 0:
                    answer_list.append(list(number_list))
                else:
                    answer_list.append(list(number_list))

                for i in range(idx, len(nums)):
                    number_list.append(nums[i])
                    dfs(number_list, i + 1)
                    number_list.pop()

            return

        dfs([],0)
        return answer_list

