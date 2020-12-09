def dfs(li):
    global check,travel_route,n,answer

    if n== len(li):
        cost=0
        for i in range(len(li)-1):
            idx=li[i]
            idx_1=li[i+1]
            if travel_route[idx][idx_1]!=0: ## 2 . 방문이 가능한 경로인지 확인
                cost+=travel_route[idx][idx_1]
            else:
                return

        start=li[0]
        end=li[len(li)-1]
        if travel_route[end][start]!=0: # 3. 맨마지막에서 처음으로 방문이 가능하면 값 갱신
            cost+=travel_route[end][start]
            answer=min(cost,answer)
        return



        return

    # 1. 모든 경우에 대해 다 돈다. 
    for i in range(n):
        if check[i]==False:
            check[i]=True
            li.append(i)
            dfs(li)
            check[i]=False
            li.pop()


answer=999999999
n=int(input())
check=[False]*n
travel_route=[0]*n
for i in range(n):
    travel_route[i]=list(map(int,input().split()))


dfs([])
print(answer)