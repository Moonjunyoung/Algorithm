class Solution:

    def dfs(self,idx,s,visited,answer):
        for i in range(idx,len(s)):
            # 1. 열린 괄호를 만나게 되면 해당 구간안으로들어감
            if s[i]=='(' and visited[i]==False:
                visited[i]=True
                self.dfs(i+1,s,visited,answer)
            # 2. 닫힌괄호를 만나게되면 해당 구간을 역으로 바꿔줌
            elif s[i]==')' and visited[i]==False:
                 visited[i]=True
                 tmp=list(answer[idx:i])
                 tmp.reverse()
                 cnt=0
                 for z in range(idx,i):
                     answer[z]=tmp[cnt]
                     cnt+=1

                 return



        return
    def reverseParentheses(self, s: str) -> str:
        visited=[False]*len(s)
        answer=[]
        tmp=""
        for i in range(len(s)):answer.append(i)

        self.dfs(0,s,visited,answer)
        for z in answer:
            if s[z].isalpha():
                tmp+=s[z]

        return tmp





a=Solution()
a.reverseParentheses("a(bcdefghijkl(mno)p)q")