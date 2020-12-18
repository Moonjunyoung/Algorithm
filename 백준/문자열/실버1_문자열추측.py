def find_answer(word): ## 해당 단어가 접미사인지 접두사인지 or 부분문자열인지판정
    global a
    answer_list=[]
    tmp=set()
    for i in a:
        prefix= word[:len(i)]
        suffix=word[-len(i):]
        if i==prefix and i==suffix:
            if i not in tmp: # 이미 있는단어면 suffix로
                tmp.add(i)
                answer_list.append('P')
            else:
                answer_list.append('S')
        elif i==prefix:
            answer_list.append('P')
        elif i==suffix:
            answer_list.append('S')
        else: ## prefix와 suffix둘다 속하지않은경우
            return False

    return answer_list

import copy
n=int(input())
tmp_list=[]
word_list=set()
for i in range(2*n-2):
    string=input()
    tmp_list.append(string)

a=copy.deepcopy(tmp_list)
tmp_list.sort()

# 1. 주어진 부분 문자열로 S를 만든다. 
for i in range(len(tmp_list)):
    for j in range(len(tmp_list)):
        if i==j:continue
        candiate_word=tmp_list[i]+tmp_list[j]
        if len(candiate_word)==n:
            word_list.add(tmp_list[i]+tmp_list[j]) # prefix
            word_list.add(tmp_list[j]+tmp_list[i]) # suffix


word_list=sorted(word_list)

# S를 만든것중에 답을 찾는다.
for i in word_list:
    flag=False
    tmp_word_pos=[]
    for j in a:
        tmp=i.find(j)
        if tmp==-1: # 부분문자열에 속하지않은경우.. 정답이 될수 x
            flag=True
            break
            
    if flag==False:
        answer_list=find_answer(i)
        if answer_list:
            print(i)
            for j in answer_list:print(j,end='')
            break