import itertools
from collections import deque
def bfs(a):
    global n,relation
    visited=[False]*(n+1)
    queue=deque()
    queue.append(a[0])
    visited[a[0]]=True
    while queue:
          cur=queue.popleft()
          for i in relation[cur]:
              if visited[i]==False and i in a: # => 연결되어있는요소가 거쳐가는것이아닌 서로 연결되어있어야 갈수있음
                 visited[i]=True
                 queue.append(i)

    for i in a:
        if visited[i]==False:
            return False

    return True

# 1.1 입력
n=int(input())
relation=[[] for _ in range(n+1)]
population=list(map(int,input().split()))
# 1-2. 연결요소 입력
for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    tmp=tmp[1:]
    for j in tmp:
        relation[i].append(j)

answer=2100000000

# 2. 선거구를 뽑는다 (1 ~N) =>
number_list=[]
for i in range(1,n+1):number_list.append(i)

for i in range(1,n//2+1):
    combination_list=list(itertools.combinations(number_list,i))
    # 2.1 선거구를 뽑는 조합을 통해 해당 경우의수가 연결이될수있는지 체크한다
    for j in combination_list:
        a=j
        b=list(set(number_list)-set(a))
        a_cnt=0
        b_cnt=0
        # 2.2 bfs를 통해 연결이되어있는지 체크한다.
        if bfs(a) and bfs(b):

           # 2.3 인구차의 최소값을 구한다.
           for z in a:
               a_cnt+=population[z-1]

           for z in b:
               b_cnt+=population[z-1]

           answer=min(answer,abs(a_cnt-b_cnt))



if answer==2100000000:
    print(-1)
else:
    print(answer)

