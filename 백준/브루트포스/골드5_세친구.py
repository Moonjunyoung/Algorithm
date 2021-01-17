from sys import stdin

n,m=map(int,stdin.readline().split())
friends=[0]*(n+1)
relation = [[False] * (n + 1) for _ in range(n + 1)]


for i in range(m):
    a,b=map(int,stdin.readline().split())
    relation[a][b]=True
    relation[b][a]=True
    friends[a]+=1
    friends[b]+=1


answer=2100000000

for i in range(1,n+1):
    for j in range(i+1,n+1):
        if relation[i][j]: # 1. A와 B가 친구이고
            for z in range(j+1,n+1):
                if relation[i][z] and relation[j][z]: #2. A와 C B와 C가 친구면 성립
                    # 3. 6을 뺴주는 이유는 각자 세사람들은  친구가 두명씩 겹침
                    answer=min(answer,friends[i]+friends[j]+friends[z]-6)



if answer==2100000000:
    print(-1)
else:
    print(answer)