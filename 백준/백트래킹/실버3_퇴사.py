# 재귀로 구현햇음
    
def dfs(sum,day,start):
    global days,cost,n,answer

    if day>n: # 1. day값이 n값보다 커버리면 그냥 종료시킴 퇴사이후니
        return

    if day+1==n+1: # 2. 그런데 day+1값이 퇴사날이랑 동일한경우 갱신
        answer=max(answer,sum)
        return

    for i in range(start,n): #3. 모든 경우를 다돔 현재꺼 고른이후부터
        dfs(sum+cost[i],days[i]+i,days[i]+i)
        answer=max(answer,sum)





n=int(input())
days=[]
cost=[]
answer=0

for i in range(n):
    a,b=map(int,input().split())
    days.append(a)
    cost.append(b)

dfs(0,0,0)
print(answer)