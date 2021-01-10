import itertools


def check(ban_id,user_id):

    if len(ban_id)!=len(user_id):
        return False

    else:
        for i in range(len(ban_id)):
            if ban_id[i]!=user_id[i]:
                if ban_id[i]!='*':
                    return False

        return True

def check_list(candidate_list,ban_list):
    cnt=0
    for i in range(len(candidate_list)):
        if check(ban_list[i],candidate_list[i]):
            cnt+=1

    if cnt==len(ban_list):
        return True


    return False



def solution(user_id, banned_id):
    answer = 0
    answer_list=[]
    candiate_list=set()
    for i in banned_id:
        for j in user_id:
            if check(i,j):
                candiate_list.add(j)

    permute_list=list(itertools.permutations(candiate_list,len(banned_id)))

    for i in permute_list:
        if check_list(i,banned_id):
           i=sorted(i)
           answer_list.append(i)


    remove_dup=list(set(map(tuple,answer_list)))

    return len(remove_dup)

