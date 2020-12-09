from itertools import combinations

# 다른사람 풀이 참조 나중에 다시풀기 

def solution(relation):
    row=len(relation)
    col=len(relation[0])

    combination_list=[]
    tmp_list=[]
    # 1 .relation column의 모든 조합을 뽑는다
    for i in range(col):tmp_list.append(i)
    for i in range(1,col+1):
        a=set(combinations(tmp_list,i))
        combination_list.extend(list(a))

    # 2. 뽑은 조합값이 column 중에 중복이 있는 지 확인한다.
    check_combination_list=[]
    for keys in combination_list:
        tmp_set=set()
        for r in range(row):
            temp = ""
            for col in keys: ##column
                temp+=relation[r][col]
            tmp_set.add(temp)

        if len(tmp_set)==row: ##중복이없다는것
            check_combination_list.append(keys)

    # 3. 최소성을 만족시키는지 확인한다. (중복 된 조합은 제거된상태 이제 부분집합만 확인하면됨)
    answer=set(check_combination_list)
    for i in range(len(check_combination_list)):
        for j in range(i+1,len(check_combination_list)):
            a=set(check_combination_list[i])
            b=set(check_combination_list[j])
            if len(a)==len(a.intersection(b)): ##부분집합인경우 지워버림
                answer.discard(check_combination_list[j])

    return len(answer)
