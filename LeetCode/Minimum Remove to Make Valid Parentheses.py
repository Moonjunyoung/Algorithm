class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        answer_list=[]
        stack=[]
        remove_list=[]
        for i in range(len(s)):
            if s[i]=='(': # 1. 열린괄호면 넣어줌
                stack.append([s[i],i])

            elif s[i]==')': # 2. 닫힌괄호일떄 쌍이 없으면 제거될 값
                 if len(stack)==0:
                     remove_list.append(i)

                 elif stack[-1][0]=='(': # 3. 쌍이존재하면 성립가능
                      stack.pop()


        while len(stack)!=0: # 4. 스택에 남아있는값은 쌍을 못찾은것이므로 제거할것들
              v,idx=stack.pop()
              remove_list.append(idx)

        for i in range(len(s)): # 5. 제거할것들을 뺴고 정답에 추가해줌
            if i not in remove_list:
                answer_list.append(s[i])


        return "".join(answer_list)
