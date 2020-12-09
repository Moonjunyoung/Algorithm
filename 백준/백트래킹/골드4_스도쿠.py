import sys
r = sys.stdin.readline

def garo_check(row,col,value): # 현재 좌표로 부터 가로열 체크
    global sudoku

    for i in range(9):
        if sudoku[row][i]==value:
            return False

    return True

def sero_check(row,col,value): #현재 좌표로 부터 세로열 체크
    global sudoku
    
    for i in range(9):
        if sudoku[i][col] == value:
            return False

    return True


def check_box(row,col,value): # 3x3 안에 중복값이 있는지확인
    global sudoku

    r=(row//3)*3
    c=(col//3)*3

    for i in range(r,r+3):
        for j in range(c,c+3):
            if value==sudoku[i][j]:
                return False

    return True

def vaild_check(row,col,value):
    if sero_check(row,col,value) and garo_check(row,col,value) and check_box(row,col,value):
        return True
    return False


def dfs(cnt):
    global board,sudoku
    if cnt== len(board):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j],end=' ')
            print()

        sys.exit(0)



    for i in range(1,10):
        row=board[cnt][0]
        col=board[cnt][1]
        if vaild_check(row,col,i): ## 해당위치에서 1~9 까지 수를 넣었을떄 스도쿠 조건에 만족시키는지확인
           sudoku[row][col]=i
           dfs(cnt+1)
           sudoku[row][col]=0


    return





board=[]
sudoku = [list(map(int, r().split())) for _ in range(9)]


for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0: ## 숫자를 채워야할 칸의 좌표를 넣음
            board.append([i,j])

dfs(0)