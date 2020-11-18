key_pad = [[0]]*4
cnt=1

## 1. 키패드판 생성
for i in range(4): key_pad[i] = [0] * 3
for i in range(4):
    for j in range(3):
        key_pad[i][j]=cnt
        cnt+=1
key_pad[3][1]=0


## 2.해당 키패드의 위치를 찾음
def find_my_location(cur): 
    global key_pad
    for i in range(4):
        for j in range(3):
            if key_pad[i][j]==cur:
                return i,j


def solution(numbers, hand):
    answer = ''
    left_hand=10
    right_hand=12
    
    for number in numbers:
        if number==1 or number==4 or number==7:
            left_hand=number
            answer+='L'
        elif number==3 or number==6 or number==9:
             right_hand=number
             answer+='R'
        
        else: # 3. 2 5 8 0 인경우 오른쪽위치와 왼쪽 위치값을 구해서 그중에서 거리가 가까운거로 누름 
             phone_x,phone_y=find_my_location(number)
             left_x,left_y=find_my_location(left_hand)
             right_x,right_y=find_my_location(right_hand)
             left_distance=abs(phone_x-left_x)+abs(phone_y-left_y)
             right_distance=abs(phone_x-right_x)+abs(phone_y-right_y)
            
             if left_distance<right_distance:
                 left_hand=number
                 answer+='L'
                 ##4. 거리가 같은경우 왼손잡이면 왼손으로 오른손잡이면 오른손으로 누름
             elif left_distance==right_distance:
                  if hand=='left':
                        left_hand=number
                        answer+='L'
                  else:
                        right_hand=number
                        answer+='R'
             else:
                right_hand=number
                answer+='R'
                
    return answer