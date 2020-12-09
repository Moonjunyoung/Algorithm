def divide(x,y,n):
    global board,answer
    if n==0:
        return

    start=board[x][y]
    flag=False

    ## 1. 영역이 모두 동일한지 확인한다.
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j]!=start:
                flag=True
                break
        if flag:break

    # 1-1. 영역이 동일하지않으면 (
    if flag==True:
        answer.append('(')
    
    # 1-2 . 영역이 동일한경우 해당 숫자를넣음 
    else:
        answer.append(start)
        return

    n=n//2
    divide(x,y,n)
    divide(x,y+n,n)
    divide(x+n,y,n)
    divide(x+n,y+n,n)
    # 1-3 모든 영역의 압축이 끝나면 닫아줌
    answer.append(')')
    



    return


answer=[]
n=int(input())
board=[0]*n

for i in range(n):board[i]=list(map(int,input()))

divide(0,0,n)

for i in answer:
    print(i,end='')