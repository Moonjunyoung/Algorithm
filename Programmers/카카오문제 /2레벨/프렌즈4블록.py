## 63점 나중에다시보기


def check_value(i, j, board):
    if board[i][j] != 0 and board[i][j + 1] != 0 and board[i + 1][j] != 0 and board[i + 1][j + 1] != 0:
        return True
    else:
        return False


def check_range(i, j, m, n):
    if i < m and j < n and i < m and j + 1 < n and i + 1 < m and j < n and i + 1 < m and j + 1 < n:
        return True
    else:
        return False


def check_bingo(i, j, board):
    if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
        return True
    else:
        return False


def fill_board(tmp_board, m, n, board):
    flag = False

    for i in range(m):
        for j in range(n):
            start_x = i
            start_y = j

            a_x = start_x
            a_y = start_y
            while True:
                if a_x >= m: break
                if tmp_board[a_x][a_y] == 1:
                    board[a_x][a_y] = board[start_x][start_y]  ##초기시작했던값을 1인위치에 넣음
                    board[start_x][start_y] = 0  ##값을 채웟으니 0으로
                    tmp_board[a_x][a_y] = 0
                    # 값을 채운위치부터 시작
                    start_x = a_x
                    start_y = a_y
                    flag = True
                elif board[a_x][a_y] == 0:
                    board[a_x][a_y] = board[start_x][start_y]  ##초기시작했던값을 안채워진 위치에 넣음
                    board[start_x][start_y] = 0

                a_x += 1

    if flag == False:
        return True, board
    else:
        return False, board


def solution(m, n, board):
    answer=0
    for i in range(m): board[i] = list(board[i])
    tmp_board = [[0]] * m
    for k in range(m): tmp_board[k] = [0] * n


    while True:
        for i in range(m):
            for j in range(n):
                if check_range(i, j, m, n):
                    if check_value(i, j, board):
                        if check_bingo(i, j, board):
                            tmp_board[i][j] = 1
                            tmp_board[i][j + 1] = 1
                            tmp_board[i + 1][j] = 1
                            tmp_board[i + 1][j + 1] = 1

        a = fill_board(tmp_board, m, n, board)
        if a[0] == True:
            break
        else:
            board = a[1]
            tmp_board = [[0]] * m
            for k in range(m): tmp_board[k] = [0] * n


    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1


    return answer