import itertools
n=int(input())
team_list=[0]*n
combination_list=[]
for i in range(n):team_list[i]=list(map(int,input().split()))
for i in range(n):combination_list.append(i)
answer=987654321

for i in combination_list:
    if i==n-1:break
    combi_list=list(itertools.combinations(combination_list,i+1))
    for j in combi_list:
        start_team = []
        link_team = []
        for z in j:start_team.append(z)
        for k in range(n):
            if k not in start_team:link_team.append(k)
    # 1. 링크팀과 스타트팀을 맞춰준다 .

        # 2. 링크팀과 스타트팀의 스코어를 계산한다.
        start_team_score=0
        link_team_score=0
        for i in range(len(start_team)):
            for j in range(i+1,len(start_team)):
                start_team_score+=team_list[start_team[i]][start_team[j]]
                start_team_score+=team_list[start_team[j]][start_team[i]]

        for i in range(len(link_team)):
            for j in range(i + 1, len(link_team)):
                link_team_score += team_list[link_team[i]][link_team[j]]
                link_team_score += team_list[link_team[j]][link_team[i]]


        answer=min(answer,abs(link_team_score-start_team_score))


print(answer)




