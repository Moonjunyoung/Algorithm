from typing import List


class Solution:
    def find_list(self,word,idx,searchWord):
        searchWord_prefix=searchWord[:idx+1]
        word_prefix=word[:idx+1]
        if searchWord_prefix==word_prefix:
            return True

        else:
            return False


    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answer_list=[]
        for i in range(len(searchWord)):
            tmp_list=[]
            for j in products:
                if self.find_list(j,i,searchWord):
                   tmp_list.append(j)


            tmp_list.sort()
            tmp_list=tmp_list[:3]
            answer_list.append(tmp_list)



        return answer_list





a=Solution()
a.suggestedProducts(["bags","baggage","banner","box","cloths"],"bags")