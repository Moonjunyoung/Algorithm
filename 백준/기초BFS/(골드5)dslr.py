def change_number(number,direction):
    ch_num=0
    if direction=='L':
       ch_num=(number%1000)*10+number//1000

    elif direction=='R':
         ch_num=(number%10)*1000+(number//10)

    elif direction=='S':
         if number==0:
            ch_num=9999
         else:
             ch_num=number-1

    elif direction=='D':
         ch_num=(number*2)%10000


    return ch_num


from collections import deque
n=int(input())

while n!=0:
    start,target=map(int,input().split())
    queue=deque()
    check=[False]*10000
    queue.append([start,''])
    check[start]=True

    while queue:
        cur_number,direction=queue.popleft()
        if cur_number==target:
            print(direction)
            break

        d=change_number(cur_number,'D')
        s=change_number(cur_number, 'S')
        l=change_number(cur_number, 'L')
        r=change_number(cur_number, 'R')

        if check[d]==False:
            check[d]=True
            queue.append([d,direction+'D'])

        if check[s] == False:
            check[s] = True
            queue.append([s, direction + 'S'])

        if check[l] == False:
            check[l] = True
            queue.append([l, direction + 'L'])

        if check[r] == False:
            check[r] = True
            queue.append([r, direction + 'R'])
    n-=1





