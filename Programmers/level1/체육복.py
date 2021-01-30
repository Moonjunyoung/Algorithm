def solution(n, lost, reserve):
    rest_cloth=dict()
    answer_list=[]

    for i in range(1,n+1):
        if i not in lost:
            answer_list.append(i)

    for i in reserve:
        rest_cloth[i]=1


    for i in lost:
        if rest_cloth.get(i)!=None:
           answer_list.append(i)
           del rest_cloth[i]


    for i in lost:
        if rest_cloth.get(i-1) !=None and i not in answer_list:
           rest_cloth[i-1]-=1
           answer_list.append(i)
           if rest_cloth[i-1]==0:
               del rest_cloth[i-1]

        elif rest_cloth.get(i+1) != None and i not in answer_list:
            rest_cloth[i+1] -= 1
            answer_list.append(i)
            if rest_cloth[i+1] == 0:
                del rest_cloth[i+1]

    print(len(answer_list))


    return len(answer_list)


solution(3,[1,2],[2,3])