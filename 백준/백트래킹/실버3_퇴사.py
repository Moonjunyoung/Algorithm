# 두번 풀음
def dfs(day,total):
    global days,cost,n,answer
    if day>n+1: ##퇴사일을 넘기면
        return

    if day==n+1: # 퇴사일다음날이면 값갱신
        answer = max(total, answer)
        return


    for i in range(day,n+1):
        dfs(i+days[i],total+cost[i]) # <여기서 실수많이함 방문시 현재 요일 + 해당요일 costday
        answer=max(total,answer)


    return

n=int(input())
days=[0]*(n+1)
cost=[0]*(n+1)
answer=0
for i in range(1,n+1):
    d,c=map(int,input().split())
    days[i]=d
    cost[i]=c

dfs(1,0)

print(answer)