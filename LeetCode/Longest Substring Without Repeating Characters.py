class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        right = len(s) - 1
        tmp = set()
        cur = 0
        while left <= right:
            if s[left] not in tmp: # 1. 현재 위치의 문자가 존재하지않을경우 넣어줌
                tmp.add(s[left])

            else: #2. 현재위치의 문자가 존재하는경우 답을 갱신하고 cur값을 하나 증가시키고 해당 cur부터 다시 찾으러감
                answer = max(answer, len(tmp))
                cur += 1
                left = cur
                tmp = set()
                continue

            left += 1

        answer = max(answer, len(tmp)) # 3. 탐색 도중 끝나는 경우가있으므로 갱신
        return answer
