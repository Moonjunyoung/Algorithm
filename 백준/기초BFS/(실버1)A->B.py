from collections import deque
a,b=map(int,input().split())

queue=deque()
queue.append([a,0])

while queue:
      number,dist=queue.popleft()

      if number==b:
          print(dist+1)
          exit(0)

      if number*2 <=b: # b보다 크면 못넣음
         queue.append([2*number,dist+1])

      if int(str(number)+str(1)) <=b: # b보다 크면 x
         queue.append([int(str(number)+str(1)),dist+1])


print(-1)