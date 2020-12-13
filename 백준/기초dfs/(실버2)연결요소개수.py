import sys
sys.setrecursionlimit(10000)

def dfs(node):
    global dist,visit
    visit[node]=True
    for i in dist[node]:
        if visit[i]==False:
            dfs(i)



n,m=map(int,input().split())
visit=[False]*(n+1)
dist=[[] for _ in range(n+1)]


answer=0
for i in range(m):
    node_1,node_2=map(int,input().split())
    dist[node_1].append(node_2)
    dist[node_2].append(node_1)

for i in range(1,n+1):
    if visit[i]==False:
        dfs(i)
        answer+=1

print(answer)