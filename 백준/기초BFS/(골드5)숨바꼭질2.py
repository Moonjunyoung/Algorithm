from collections import deque

n,k=map(int,input().split())
dist=[0]*100001
check=[False]*100001
queue=deque()
queue.append(n)
dist[n]=0
check[n]=True

answer_cnt=[0]*100001
answer_cnt[n]=1
while queue:
      cur_pos=queue.popleft()

      if cur_pos * 2 < 100001 and check[cur_pos * 2] == False:
          check[cur_pos * 2] = True
          queue.append(cur_pos * 2)
          dist[2 * cur_pos] = dist[cur_pos] + 1
          answer_cnt[cur_pos * 2] = 1
      elif cur_pos * 2 < 100001 and dist[cur_pos * 2] != 0: # 가중치가 존재하는경우 
          if dist[cur_pos * 2] == dist[cur_pos] + 1:
              queue.append(cur_pos*2)
              answer_cnt[cur_pos * 2] += 1

      if cur_pos-1>=0 and check[cur_pos-1]==False:
          check[cur_pos-1]=True
          queue.append(cur_pos-1)
          dist[cur_pos-1]=dist[cur_pos]+1
          answer_cnt[cur_pos-1]=1
      elif cur_pos-1>=0 and dist[cur_pos-1]!=0:
           if dist[cur_pos-1]==dist[cur_pos]+1:
               queue.append(cur_pos-1)
               answer_cnt[cur_pos-1]+=1

      if cur_pos+1<100001 and check[cur_pos+1]==False:
          check[cur_pos+1]=True
          queue.append(cur_pos+1)
          dist[cur_pos+1]=dist[cur_pos]+1
          answer_cnt[cur_pos + 1] = 1
      elif cur_pos+1<100001 and dist[cur_pos+1]!=0:
           if dist[cur_pos+1]==dist[cur_pos]+1:
               queue.append(cur_pos+1)
               answer_cnt[cur_pos+1]+=1



print(dist[k])
print(answer_cnt[k])


