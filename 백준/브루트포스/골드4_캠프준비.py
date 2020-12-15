def check_answer(sum,max_problem,min_problem): #1. 문제 조건이 맞는지 확인
    global l,r,x
    if max_problem-min_problem<x:return False
    if sum<l or sum>r:return False
    return True


import itertools
n,l,r,x=map(int,input().split())
problem_list=list(map(int,input().split()))
answer=0
cnt=1
while cnt<=n:
    combination_list=list(itertools.combinations(problem_list,cnt)) # 2. 모든 문제를 뽑는경우를 찾음
    for i in combination_list:
        sum=0
        for j in i:sum+=j
        if check_answer(sum,max(i),min(i)):
            answer+=1
    cnt+=1

print(answer)
