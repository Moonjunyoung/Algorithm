# 다른 사람 풀이 참조 완탐돌렸다가 메모리초과 나옴 
# 1. 싸이클이 이루어진 수들이 최대 뽑을수있는 수다.

def dfs(current_number,start_number):
    global number_list,visited
    if visited[current_number] and current_number==start_number:#싸이클이이루어지면
       answer_list.append(start_number)
       return

    if visited[current_number]==False:
        visited[current_number]=True
        dfs(number_list[current_number],start_number)

    return

n=int(input())
number_list=[0]*(n+1)
answer_list=[]
for i in range(1,n+1):
    tmp=int(input())
    number_list[i]=tmp

for i in range(1,n+1):
    visited=[False]*(n+1)
    dfs(i,i)

answer_list.sort()
print(len(answer_list))
for i in answer_list:print(i)