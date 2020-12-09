#풀이 참조 나중에 다시풀기..

from collections import deque



a,b,c=map(int,input().split())

check=[False]*201
answer=[]
ans=[False]*201
for i in range(201):check[i]=[0]*201

queue=deque()
queue.append([0,0,c])

# 총 6가지의 이동할수있는 경우에대해 bfs를 돌려줌

while queue:
      da,db,dc=queue.popleft()
      if da==0: ##a의 물양이 0 일떄 현재 c의값 즉 답
          ans[dc]=True

      if check[da][db]==True:continue
      check[da][db]=True

      # 1. a->b로 옮길떄
      if da+db>b : # b값이 꽉차면
          queue.append([(da+db)-b,b,dc])
      else:
          queue.append([0,da+db,dc])

      # 2. a->c로 옮길떄
      if da+dc>c:
          queue.append([(da+dc)-c,db,c])
      else:
          queue.append([0,db,da+dc])

      #3. b->a로 올길떄
      if db+da>a:
          queue.append([a,(db+da)-a,dc])
      else:
          queue.append([db+da,0,dc])

      #4 b->c로 옮길떄
      if db+dc>c:
          queue.append([da,(db+dc)-c,c])
      else:
          queue.append([da,0,db+dc])

      #5 c->a로 옮길떄
      if dc+da>a:
          queue.append([a,db,(dc+da)-a])
      else:
          queue.append([dc+da,db,0])
      #6 c->b로 옮길떄
      if dc+db>b:
          queue.append([da,b,(dc+db)-b])
      else:
          queue.append([da,dc+db,0])



for i in range(201):
    if ans[i]==True:
        answer.append(i)

answer.sort()
for i in answer:
    print(i,end=' ')