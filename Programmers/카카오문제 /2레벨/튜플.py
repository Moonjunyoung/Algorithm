import re

def solution(s):
    
    answer = []
    li=re.findall('\d+',s) ## 1. 정규표현식을 사용해서 숫자만 남겨놓음
    dic={}
   
    #2. 숫자가 의 빈도수를 딕셔너리에 담음
    for i in li:dic[int(i)]=0
    for i in li: dic[int(i)]+=1
   

    #3. 숫자 빈도가 많은순으로 내림차순 정렬  숫자 빈도가 많은게 가장 맨앞으로 옴
    dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
   
    for a in dic:answer.append(a[0])
   
   
    
    return answer