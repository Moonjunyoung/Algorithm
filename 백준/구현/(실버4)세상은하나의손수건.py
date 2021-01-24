n,end=map(int,input().split())
t=n
cur_x=0
cur_y=0
dir=0
prev=0

while t!=0:
      pos,d=map(str,input().split())
      pos=int(pos)

      next_pos = pos -prev # 1. 이전 위치와 현재 위치를 뻄으로 다음에 이동할곳알수있다.
      prev=pos


      # 2. 방향에 따른 이동방법
      if dir == 0:  # 오른쪽 ->
          cur_x += next_pos
      elif dir == 1: # 아래
          cur_y -= next_pos
      elif dir == 2:# 왼쪽 <-
          cur_x -= next_pos
      elif dir == 3:# 위
          cur_y += next_pos

      # 3. 방향을 바꿔줌
      if d=='right':
          dir=(dir+1)%4

      elif d=='left':
           dir=(dir-1)%4

      t-=1

next_pos=end-prev
if dir == 0:
    cur_x += next_pos
elif dir == 1:
    cur_y -= next_pos
elif dir == 2:
    cur_x -= next_pos
elif dir == 3:
    cur_y += next_pos


print(cur_x,cur_y)