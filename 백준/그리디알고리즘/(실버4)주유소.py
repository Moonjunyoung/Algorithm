n=int(input())
dist=list(map(int,input().split()))
cost=list(map(int,input().split()))

min_cost=cost[0]
answer=min_cost*dist[0]

# 문제해결방법 : 최소 비용으로 마지막까지 가려면 이동하면서 최소비용의금액으로 연료를 채우면된다.
for i in range(1,n-1):
    if cost[i]<min_cost: # 1 .현재 주요소 비용이 최소비용으로 갱신이가능하면
        min_cost=cost[i]

    answer+=min_cost*dist[i]


print(answer)