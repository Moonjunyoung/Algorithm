https://www.acmicpc.net/problem/2630 와 개똑같은 문제

answer_list={}
answer_list[1]=0
answer_list[0]=0
def check(arr,x,y,n):
    pivot=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=pivot:
                return [False,-1]


    return [True,1,pivot]

def divide(arr,size,x,y):
    global answer_list
    tmp=check(arr,x,y,size)
    if tmp[0]==True:
        answer_list[tmp[2]]+=tmp[1]
        return

    else:
        size=size//2
        divide(arr,size,x,y)
        divide(arr,size,x,size+y)
        divide(arr,size,x+size,y)
        divide(arr,size,x+size,y+size)



def solution(arr):
    answer = []

    divide(arr,len(arr),0,0)

    answer.append(answer_list[0])
    answer.append(answer_list[1])

    return answer



solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])

