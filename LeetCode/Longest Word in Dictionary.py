class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        answer_list=[]
        for i in d:
            target=i
            l=0
            r=0
            end=len(target)
            while l<len(s) and r<end:
                  if s[l]==target[r]:
                     l+=1
                     r+=1
                  else:
                      l+=1

            if r==end:
                answer_list.append([target,len(target)])

        answer_list=sorted(answer_list,key=lambda x:(-x[1],x[0]))

        if len(answer_list)==0:
            return " "

        return answer_list[0][0]
