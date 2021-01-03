from collections import deque
def left_wheel(current_wheel,rot):
    global wheel,left_rotate_list

    if current_wheel-1<0: #범위를 벗어난 톱니
        return

    if wheel[current_wheel][6]!=wheel[current_wheel-1][2]:
       #wheel[current_wheel-1].rotate(rot)
       left_rotate_list.append([current_wheel-1,rot])
       left_wheel(current_wheel-1,-rot)

    return


def right_wheel(current_wheel,rot):
    global wheel,t,right_rotate_list
    if current_wheel + 1 >=t:  # 범위를 벗어난 톱니
        return

    if wheel[current_wheel][2] != wheel[current_wheel + 1][6]:
        #wheel[current_wheel + 1].rotate(rot)
        right_rotate_list.append([current_wheel+1,rot])
        right_wheel(current_wheel + 1, -rot)

    return


t=int(input())

wheel=[]
for i in range(t):
    tmp=list(map(int,input()))
    wheel.append(deque(tmp))
command=int(input())
while command!=0:
      wheel_number,direction=map(int,input().split())
      wheel_number-=1
      left_rotate_list=[]
      right_rotate_list=[]

      # 1.왼쪽에 돌아갈수있는 톱니바퀴를 찾는다.
      left_wheel(wheel_number,-direction)
      # 2. 오른쪽에 돌아갈수있는 톱니바퀴를찾는다.
      right_wheel(wheel_number,-direction)

      for i in range(len(left_rotate_list)):
          number,d=left_rotate_list[i]
          wheel[number].rotate(d)

      for i in range(len(right_rotate_list)):
          number, d = right_rotate_list[i]
          wheel[number].rotate(d)

      wheel[wheel_number].rotate(direction)
      command-=1

answer=0
for i in range(t):
    if wheel[i][0]==1: #12시방향이 s극인 톱니바퀴의 개수
        answer+=1


print(answer)