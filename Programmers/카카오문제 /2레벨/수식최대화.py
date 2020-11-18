import re
from itertools import permutations

def solution(expression):
    answer = 0
    answer_list=[]
    op=re.findall("\D",expression) ##1. operation만을 추출
    permute=list(permutations(set(op))) #2. operation 중복제거 (중복이있으면 나중에 연산할떄 지장이 생기므로 중복제거)
    #2.1 operation의 모든 순열들을 구함
 

    for i in permute:
        tmp_op=list(i)  ## 2.2 operation의 순열들중 하나를 뻄
        temp = re.compile("(\D)").split('' + expression)  #2.3 다른사람꺼보고 참조 들어오는 입력을 원하는 리스트로 쪼개줌
        ##숫자와 비문자를 각각 짤라줌
        
        
        total=0
        for exp in tmp_op:
            idx=0
            while True:
                if exp not in temp:break ## 2.4 연산자가 더이상 존재하지않으면 종료시킴 (계산이 끝난것이므로)
                value=temp[idx%len(temp)] # 2.5 idx range out 방지
                if value==exp :# 2.6 우선순위에 해당되는 연산이면
                    a = int(temp[idx - 1])
                    b = int(temp[idx + 1])
                    if exp=="-": ## 2.7 그거에 맞게 계산을해줌 여기서 좀 해맴 앞으로 리스트 갱신 시키는것은 for문아닌 while문으로 해야겠음
                        total=a-b
                        temp[idx]=str(total)
                    elif exp=='*':
                        total = a * b
                        temp[idx]=str(total)
                    elif exp=='+':
                        total = a + b
                        temp[idx]=str(total)

                    temp.pop(idx - 1)
                    temp.pop(idx)
                else:
                    idx+=1

        answer_list.append(abs(int(temp[0])))

    print(answer_list)
    answer=max(answer_list)

    return answer