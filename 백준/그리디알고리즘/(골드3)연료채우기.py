import heapq
from collections import deque

n=int(input())
joyouso_list=[]
possible_list=[]
for i in range(n):
    a,b=map(int,input().split())
    joyouso_list.append([a,b])

# 맨 마지막 입력은 마을까지의 거리와 시작 현재 연료의상태 를준다.
town_pos,cur_fuel=map(int,input().split())
joyouso_list.sort()
joyouso_list=deque(joyouso_list)
answer=0

# 문제 해결방법 주핵심  : 1. 갈수있는 주유소 들중에 연료를 가장 많이채울수있는곳을 들려서 연료를 채운다 .

while cur_fuel<town_pos:
      while joyouso_list:
            loc,fuel=joyouso_list.popleft()
            # 2. 갈수있는곳이면 가장 많이 채울수 있는 연료 순으로 우선순위큐에 저장
            if loc<=cur_fuel:
                heapq.heappush(possible_list,-fuel)
            else:
                 joyouso_list.appendleft([loc,fuel])
                 break


      if len(possible_list)==0:
          answer=-1
          break # 1. 갈수있는곳이 존재하지 x

      f=heapq.heappop(possible_list)*-1
      cur_fuel+=f
      answer+=1


print(answer)


