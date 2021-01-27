import itertools

def check_list(food_list,orders):
    answer=0
    a=set(food_list)
    for i in orders:
        b=a.intersection(set(i))
        if len(a)==len(b):
            answer+=1

    return answer


def solution(orders, course):
    answer = set()

    for i in course:
        a=[]
        for order in orders:
            combination_list=list(itertools.combinations(sorted(order),i))
            for j in combination_list:
                count=check_list(j,orders)
                if count>=2:
                    a.append(["".join(j), count])

        a = sorted(a, key=lambda x: -x[1])
        if len(a) == 0: continue
        max_value = a[0][1]
        for z in a:
            if max_value == z[1]:
               answer.add(z[0])
            else:break


    answer = list(answer)
    answer.sort()

    return answer





