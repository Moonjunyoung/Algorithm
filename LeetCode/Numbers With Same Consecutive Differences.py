class Solution:
    
    def dfs(self,depth,n,k,number,answer):
        if depth==n:
            answer.append(number)
            return

        for i in range(10):
            if depth==0 and i==0:continue
            if depth==0 and i>=1:
                self.dfs(depth+1,n,k,number+str(i),answer)
            else:
                tmp=abs(int(number[depth-1])-i)
                if tmp!=k:continue
                self.dfs(depth+1,n,k,number+str(i),answer)
        
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer=[]
        self.dfs(0,n,k,"",answer)
        return answer
        