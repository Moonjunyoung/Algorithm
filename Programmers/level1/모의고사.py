def solution(answers):
    answer = dict()
    human_1=[1,2,3,4,5]
    human_2=[2,1,2,3,2,4,2,5]
    human_3=[3,3,1,1,2,2,4,4,5,5]

    for i in range(1,4):answer[i]=0

    for i in range(len(answers)):
        one=human_1[i%5]
        two=human_2[i%8]
        three=human_3[i%10]
        if one==answers[i]:
           answer[1]+=1

        if two==answers[i]:
           answer[2]+=1

        if three==answers[i]:
            answer[3]+=1

    answer_list=[]
    value=sorted(answer.items(),key= lambda x:x[1],reverse=True)
    max_value=value[0][1]
    for i in range(1,4):
        if max_value==answer[i]:
            answer_list.append(i)



    return answer

solution([1,2,3,4,5])