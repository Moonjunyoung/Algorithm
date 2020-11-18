# 문제 이해 병신같이해서 존나 해맨문제 나중에 꼭 다시풀기

# 이해 잘못했던부분 = 현재 시간을고르면 그 시간 이후로는 모두 선택이 가능한데 계속 병신짓함

import itertools

n=int(input())
day=[]
cost=[]

for i in range(n):
    a,b=map(int,input().split())
    day.append(a)
    cost.append(b)

answer=0
tmp=[]
for i in range(n):tmp.append(i)

for i in range(n,0,-1):
    combination = list(itertools.combinations(tmp,i)) ## 총 n~0까지의 조합을 만들면서 모든경우를 다확인
    for j in combination:
        visit_list=[]
        time=j[0] ##time은 현재로 정함
        for idx,value in enumerate(j):   
            if time<=value:  # 1. 시간이 정해지면 그시간 보다 큰 시간은 모두 방문이 가능함
                if value+day[value]<=n: ## 2 . 해당경우의 시간 + 그 시간을 골랐을떄 다음으로 이동한시간 값이 n보다 작거나 같아야됨 그래야 이동가능 
                    time=value+day[value]  # 2.1 이동이가능하면 이동가능한시간으로 다시 초기화
                    visit_list.append(cost[value]) # 2.2 cost넣어줌




        answer=max(answer,sum(visit_list))


print(answer)