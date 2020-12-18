from collections import deque
n,m=map(int,input().split())
visited=[False]*101
scores=[0]*101
for i in range(n+m):
    a,b=map(int,input().split())
    scores[a]=b

queue=deque()
queue.append([1,0])
visited[1]=True


# 이동한 좌표가 사다리나 뱀이 있는경우는 무조건 그쪽으로 이동해야됨 안그러면 wrong answer
while queue:
      cur_pos,dist=queue.popleft()
      if cur_pos==100:
          print(dist)
          exit(0)

      if cur_pos+1<=100:
          if scores[cur_pos+1]!=0:
             queue.append([scores[cur_pos+1],dist+1])
          elif visited[cur_pos+1]==False:
               visited[cur_pos+1]=True
               queue.append([cur_pos+1,dist+1])

      if cur_pos+2<=100:
          if scores[cur_pos+2]!=0:
             queue.append([scores[cur_pos+2],dist+1])
          elif visited[cur_pos+2]==False:
               visited[cur_pos+2]=True
               queue.append([cur_pos+2,dist+1])

      if cur_pos+3<=100:
          if scores[cur_pos+3]!=0:
             queue.append([scores[cur_pos+3],dist+1])
          elif visited[cur_pos+3]==False:
               visited[cur_pos+3]=True
               queue.append([cur_pos+3,dist+1])

      if cur_pos+4<=100:
          if scores[cur_pos+4]!=0:
             queue.append([scores[cur_pos+4],dist+1])
          elif visited[cur_pos+4]==False:
               visited[cur_pos+4]=True
               queue.append([cur_pos+4,dist+1])

      if cur_pos+5<=100:
          if scores[cur_pos+5]!=0:
             queue.append([scores[cur_pos+5],dist+1])
          elif visited[cur_pos+5]==False:
               visited[cur_pos+5]=True
               queue.append([cur_pos+5,dist+1])

      if cur_pos+6<=100:
          if scores[cur_pos+6]!=0:
             queue.append([scores[cur_pos+6],dist+1])
          elif visited[cur_pos+6]==False:
               visited[cur_pos+6]=True
               queue.append([cur_pos+6,dist+1])
