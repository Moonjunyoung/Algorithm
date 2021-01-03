from collections import deque
def game_over():
    global convey_belt,k
    cnt=0
    for i in convey_belt:
        if i==0:cnt+=1

    if cnt>=k:
        return False
    else:
        return True

n,k=map(int,input().split())
convey_belt=list(map(int,input().split()))
answer=0
convey_belt=deque(convey_belt)
visited= [False] * len(convey_belt)
visited=deque(visited)
while True:

      # 1. 벨트를 한칸 회전한다. n-1 = 컨베이어 벨트 상단 끝 회전했으니 상단끝에 로봇이존재할수도있으니 False
      convey_belt.rotate(1)
      visited.rotate(1)
      visited[n-1]=False

      # 2. 가장 먼저 벨트 위에 올라간 로봇들 중에 이동할수있는것을 살핀다.
      # 2.1 컨베이어 벨트 상단의 로봇들을 체킹 (길이가 n)

      # 현재위치가 로봇이 존재하고 , 다음칸이 로봇이 x , 다음칸의 내구도가 1이상인경우
      # n-2 즉 상단끝 전 원소 부터 시작
      for i in range(n-2,-1,-1):
          if visited[i] and visited[i+1]==False and convey_belt[i+1]>0:
              visited[i]=False
              visited[i+1]=True
              convey_belt[i+1]-=1

      # 2.2 컨베이어 상단 끝에 로봇이 있는경우 로봇을 밑으로 내린다.
      visited[n-1] = False

      # 3. 올라가있는 위치 (0) 에 로봇이 없다면 로봇을 하나 올린다.
      if visited[0]==False and convey_belt[0]>0:
         visited[0]=True
         convey_belt[0]-=1

      answer+=1

      if game_over()==False:
          break



print(answer)