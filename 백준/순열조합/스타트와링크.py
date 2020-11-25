# 완전탐색으로 안풀려서 combination 사용 

import itertools
n=int(input())

score=[0]*n
check=[0]*n
for i in range(n):score[i]=list(map(int,input().split()))
for i in range(n):check[i]=i


start_team_list=list(itertools.combinations(check,n//2))
answer=9999999999

for i in start_team_list: 
    start_team=set(i)
    link_team=set(check)-set(start_team) 
    start_team=list(start_team)
    link_team=list(link_team)
    start_team_score=0
    link_team_score=0
    for i in range(len(start_team)): ##점수계산하는부분
        for j in range(i,len(start_team)):
            start_team_score+=score[start_team[i]][start_team[j]]+score[start_team[j]][start_team[i]]
            link_team_score+=score[link_team[i]][link_team[j]]+score[link_team[j]][link_team[i]]


    answer=min(abs(start_team_score-link_team_score),answer)

print(answer)





