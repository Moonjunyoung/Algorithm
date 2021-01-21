
t=int(input())
def check_distance(c_x,c_y,t_x,t_y):
    distance=abs(c_x-t_x)+abs(c_y-t_y)
    if distance<=1000:
        return True
    return False

def dfs(cur):
    global visited,graph
    visited[cur]=True
    for i in graph[cur]:
        if visited[i]==False:
            dfs(i)

while t!=0:
      v=int(input())
      graph=[0]*(v+2)
      visited=[False]*(v+2)
      for i in range(v+2):
          graph[i]=list()
      li=[]
      for i in range(v+2):
          x,y=map(int,input().split())
          li.append([x,y])


      # 1. 정점으로부터 연결할수있는 거리 1000m이하 인것들끼리 연결시킴
      for i in range(v+2):
          c_x,c_y=li[i]
          for j in range(i+1,v+2):
              nx,ny=li[j]
              if check_distance(c_x,c_y,nx,ny):
                 graph[i].append(j)
                 graph[j].append(i)

      #2. 집부터 시작해서 연결된정점으로 이동하면서 락페스티벌에 도착할수있는지 확인
      dfs(0)
      # 3. 도착할수있으면 
      if visited[v+1]:
          print("happy")
      else:
          print("sad")


      t-=1
