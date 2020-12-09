
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numOfAllPlayers=int(input())
numOfQuickPlayers=int(input())
namesOfQuickPlayers=list(input().split())
numOfGames=int(input())
numOfMovesPerGame=list(input().split())

# 1.모든 플레이어 수 만들기
player_list=[0]*numOfAllPlayers
quick_player_list=[False]*26

#가장 빠른 플레이어 리스트
for i in namesOfQuickPlayers:quick_player_list[ord(i)-65]=True


cnt=0
player_list[0] += 1
# A가 처음엔 무조건 술래
cur_state=[]
cur_sulrae=0 ##현재술래
cur_sulrae_pos=0
next_state=0
for i in range(1, numOfAllPlayers): cur_state.append(i)
while cnt!=numOfGames:
    next_state=(cur_sulrae_pos+int(numOfMovesPerGame[cnt]))%(numOfAllPlayers-1)## 1. 현재술래 위치 + 다음에 이동할위치

    if quick_player_list[cur_state[next_state]]==False: ## 2 현재술래가 다음술래를 따라잡을수있다면
        tmp=cur_state[next_state]
        cur_state[next_state]=cur_sulrae ## 다음술래의 위치에 현재술래를 넣음
        player_list[tmp]+=1  #다음술래 는 술래가됨
        cur_sulrae_pos=next_state # 현재술래의 위치 갱신
        cur_sulrae=tmp ##다음술래는 술래

    else: ## 현재술래가 다음술래를 따라잡을수없다면
        cur_sulrae_pos=next_state ## 현재술래의 위치를 다음술래의 위치로 갱신
        player_list[cur_sulrae]+=1 # 현재술래값 증가


    cnt+=1

cur_state.append(cur_sulrae)

for i in cur_state:
    print(alpha[i],player_list[i],end=' ')
    print()

