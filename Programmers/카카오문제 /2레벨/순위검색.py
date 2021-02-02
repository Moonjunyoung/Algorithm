import bisect


language=['-','cpp','java','python']
jobs=['-','frontend','backend']
career=['-','junior','senior']
food=['-','chicken','pizza']




def solution(info, query):
    answer = []
    info_list={}

    # 1. 들어오는 info 하나 당 16개의 경우의 쿼리를 만족하므로 이에 해당하는 값을 구해준다
    for i in info:
        array=i.split(' ')
        l,j,c,f,price=array[0],array[1],array[2],array[3],array[4]
        l=language.index(l)
        j=jobs.index(j)
        c=career.index(c)
        f=food.index(f)
        price=int(price)

        #  16개의 쿼리를 구하는 반복문
        for l1 in [0,l]:
            for j1 in [0,j]:
                for c1 in [0,c]:
                    for f1 in [0,f]:
                        info_query=language[l1]+jobs[j1]+career[c1]+food[f1]
                        if info_query not in info_list:
                            info_list[info_query]=[price]
                        else:
                             info_list[info_query].append(price)


    #  해당 쿼리의 price 값을 빨리 조회하기 위해 이분탐색 사용
    for key in info_list:info_list[key].sort()


    # 들어오는 쿼리 를 만족시키는 값을 딕셔너리에서 찾는다 .
    for i in query:
        array=i.split(' ')
        l,j,c,f,price=array[0],array[2],array[4],array[6],array[7]
        l = language.index(l)
        j = jobs.index(j)
        c = career.index(c)
        f = food.index(f)
        price=int(price)
        info_query = language[l] + jobs[j] + career[c] + food[f]
        if info_query not in info_list:
            answer.append(0)
        else:
            member=len(info_list[info_query])-bisect.bisect_left(info_list[info_query],price) # 전체 값 - price보다 작은값 = price 이상의값
            answer.append(member)



    return answer






solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])