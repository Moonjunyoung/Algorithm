def check_block(block_list,row,col,color,max_r,max_c):

    remove_list=[]

    for i in range(row,row+2):
        for j in range(col,col+2):
            if i>=max_r or j>=max_c or block_list[i][j]==0:
               return [False,-1]

            if block_list[i][j]==color :
               remove_list.append([i,j])


    if len(remove_list)==4:
       return [True,remove_list]
    else:
        return [False,-1]

def find_remove_block(m,n,board):
    remove_list=[]
    for i in range(m):
        for j in range(n):
            flag=check_block(board,i,j,board[i][j],m,n)
            if flag[0]:
                remove_list.append(flag[1])



    if len(remove_list)!=0:
        for i in remove_list:
            for j in i:
                x,y=j
                board[x][y]=0
        return True

    else:
        return False



def change_map(tmp_board,column,max_r,board):
    tmp_board.reverse()
    for i in range(max_r):
        board[i][column]=tmp_board.pop(0)





def move_down(r,c,board):

    for i in range(c):
        tmp_list=[]
        for j in range(r):
            tmp_list.append(board[j][i])

        cnt=0
        idx=0
        tmp_list.reverse()
        while idx<r and cnt<r:
              if tmp_list[idx]==0:
                 tmp_list.append(tmp_list.pop(idx))
                 idx-=1
                 cnt+=1

              idx+=1

        change_map(tmp_list,i,r,board)


    return



def solution(m, n, board):
    answer = 0
    for i in range(m):
        tmp=list(board[i])
        board[i]=tmp

    while True:
          if find_remove_block(m,n,board):
             move_down(m,n,board)
          else:
              break

    for i in range(m):
        for j in range(n):
            if board[i][j]==0:
                answer+=1


    return answer

