def solution(participant, completion):
    answer = ''
    dic={}
    for i in participant:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1

    for i in completion:
        if i in dic:
            dic[i]-=1
            if dic[i]==0:
                del dic[i]

    answer=dic.popitem()[0]

    return answer