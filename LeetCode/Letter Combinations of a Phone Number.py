class Solution:
    answer_list=[]
    alpha_list=[[0],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],                ['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    
    def dfs(self,idx,string,digits):
        if len(string)==len(digits):
            self.answer_list.append(string)
            return
        else:
            number=int(digits[idx])-1
            for i in self.alpha_list[number]:
                for j in i:
                    self.dfs(idx+1,string+j,digits)
                    
        
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        else:
             self.answer_list=[]
             self.dfs(0,"",digits)
             
        
        return self.answer_list