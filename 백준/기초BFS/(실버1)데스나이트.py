from collections import deque
n=int(input())
r1,c1,r2,c2=map(int,input().split())

queue=deque()
visited=[False]*300
for i in range(300):
    visited[i]=[False]*300

queue.append([r1,c1,0]) #데스나이트 현재위치
while queue:
      cur_x,cur_y,dist=queue.popleft()
      if cur_x==r2 and cur_y==c2:
          print(dist)
          exit(0)

      if cur_x-2>=0 and cur_y-1>=0 and visited[cur_x-2][cur_y-1]==False:
          visited[cur_x-2][cur_y-1]=True
          queue.append([cur_x-2,cur_y-1,dist+1])

      if cur_x-2>=0 and cur_y+1<n and visited[cur_x-2][cur_y+1]==False:
          visited[cur_x-2][cur_y+1]=True
          queue.append([cur_x-2,cur_y+1,dist+1])

      if cur_x>=0 and cur_y-2>=0 and visited[cur_x][cur_y-2]==False:
          visited[cur_x][cur_y-2]=True
          queue.append([cur_x,cur_y-2,dist+1])

      if cur_x>=0 and cur_y+2<n and visited[cur_x][cur_y+2]==False:
          visited[cur_x][cur_y+2]=True
          queue.append([cur_x,cur_y+2,dist+1])

      if cur_x+2<n and cur_y-1>=0 and visited[cur_x+2][cur_y-1]==False:
          visited[cur_x+2][cur_y-1]=True
          queue.append([cur_x+2,cur_y-1,dist+1])

      if cur_x+2<n and cur_y+1<n and visited[cur_x+2][cur_y+1]==False:
         visited[cur_x+2][cur_y+1]=True
         queue.append([cur_x+2,cur_y+1,dist+1])

print(-1)