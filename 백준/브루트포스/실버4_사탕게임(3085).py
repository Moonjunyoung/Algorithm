dx=[0,0,1,-1]
dy=[-1,1,0,0]
#좌 우 하 상
answer=0
def check(score):
    global answer

    #모든 맵을 다 탐색함 (이렇게안하면 wa 뜨길래)
    for i in range(len(score)):
        for j in range(len(score)):
            cur=score[i][j]
            garo_cnt = 1
            for z in range(j+1,len(score)):
                if cur==score[i][z]:
                    garo_cnt+=1
                else:
                    break
            answer=max(answer,max(garo_cnt,answer))
        ## 가로 탐색

        # 세로 탐색
    for i in range(len(score)):
        for j in range(len(score)):
            cur = score[j][i]
            sero_cnt = 1
            for z in range(j + 1, len(score)):
                if cur == score[z][i]:
                    sero_cnt += 1
                else:
                    break
            answer = max(answer, max(sero_cnt, answer))


n=int(input())
candy=[0]*n

for i in range(n):
    a=list(map(str,input().split()))
    a=list(a[0])
    candy[i]=a


for i in range(n):
    for j in range(n):
        ## 1. 상하 좌우를 돌면서 바꿀수있는 캔디가 있는지 확인
        for z in range(4):
            da=dx[z]+i
            db=dy[z]+j
            if da<0 or db<0 or da>=n or db>=n:
                continue
            else: ## 2. 바꿀수있는 캔디면 캔디를 바꾼뒤 해당 맵 체크
                tmp=candy[i][j]
                tmp2=candy[da][db]
                candy[i][j]=tmp2
                candy[da][db]=tmp
                check(candy)
                candy[i][j]=tmp
                candy[da][db]=tmp2


print(answer)