from collections import deque

def bfs(weight):
    global factory_a,visited,bridge_list,factory_b
    queue=deque()
    queue.append(factory_a)
    visited[factory_a]=True


    while queue:
          cur=queue.popleft()

          if factory_b==cur:
              return True

          for i in bridge_list[cur]:
              next,cost=i
              if visited[next]==False and cost>=weight: # 1.이분탐색으로 찾은 비용 보다 작은경우에 방문가능
                 visited[next]=True
                 queue.append(next)


    return False

n,m=map(int,input().split())

bridge_list=[[] for _ in range(n+1)]

left=1
right=-9999999
for i in range(m):
    a,b,c=map(int,input().split())
    right=max(c,right)
    bridge_list[a].append([b,c])
    bridge_list[b].append([a,c])

factory_a,factory_b=map(int,input().split())

answer=0
while left<=right:
      visited = [False] * (n + 1)
      mid= (left+right)//2

      if bfs(mid):
          answer=max(mid,answer)
          left=mid+1
      else:
          right=mid-1

print(answer)