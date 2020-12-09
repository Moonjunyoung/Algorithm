from collections import deque
import copy
wheels=[0]*4
for i in range(4):wheels[i]=list(map(int,input()))
k=int(input())

def change(cur,direction):
    global wheels
    dq=deque(list(wheels[cur]))
    dq.rotate(direction)
    wheels[cur]=copy.copy(dq)



def left(cur,direction): # 1. 현재바퀴에서 왼쪽에있는것들만 처리
    global wheels
    if cur<0:
        return

    if wheels[cur][2]!=wheels[cur+1][6]:
        left(cur-1,-direction)
        change(cur,direction)

def right(cur,direction): # 1. 현재바퀴에서 오른쪽에있는것들만 처리
    global wheels
    if cur>3:
        return

    if wheels[cur-1][2]!=wheels[cur][6]:
        right(cur+1,-direction)
        change(cur,direction)


while k!=0:
    rotate_wheel,direction=map(int,input().split())
    rotate_wheel-=1

    # 1. 현재 바퀴에서 왼쪽 바퀴 에있는것들만 처리
    left(rotate_wheel-1,-direction)

    # 2. 현재바퀴에서 오른쪽 바퀴에있는것들만 처리
    right(rotate_wheel+1,-direction)

    #3. 현재바퀴는 마지막에 처리
    change(rotate_wheel,direction)



    k-=1

score=0

if wheels[0][0]==1:
    score+=1
if wheels[1][0]==1:
    score+=2
if wheels[2][0]==1:
    score+=4
if wheels[3][0]==1:
    score+=8

print(score)