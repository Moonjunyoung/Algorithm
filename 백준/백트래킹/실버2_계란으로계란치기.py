def dfs(cur):
    global egg_state,egg_weight,n,answer

    if cur==n:
        cnt=0
        for i in egg_state: # 맨마지막 위치에 가면 꺠진계란의수를 샘
            if i<=0:cnt+=1 
        answer=max(cnt,answer) 
        return

    if egg_state[cur]<=0: ##계란을 꺨수없으면 다음계란으로넘김
        dfs(cur+1)
        return

    flag=False #(계란을 꺨수있는지 없는지 확인하는 flag)
    for i in range(n):
        if i==cur or egg_state[i]<=0: ##현재 자신의 계란이거나 깨진계란이면 skip
            continue
        egg_state[cur]=egg_state[cur]-egg_weight[i] ##꺨수있으면 상대방꺼와 부딪힘
        egg_state[i]=egg_state[i]-egg_weight[cur]
        flag=True
        dfs(cur+1)
        egg_state[cur]=egg_state[cur]+egg_weight[i] ##원상복구
        egg_state[i]=egg_state[i]+egg_weight[cur]

    if flag==False: ##현재 위치에서 계란을 꺨수없는 경우 마지막으로가서 카운팅
        dfs(n)
        return

n=int(input())
egg_state=[]
egg_weight=[]
answer=0
for i in range(n):
    a,b=map(int,input().split())
    egg_state.append(a)
    egg_weight.append(b)



dfs(0)

print(answer)
