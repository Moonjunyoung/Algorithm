from typing import List


class Solution:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    row=0
    col=0

    def dfs(self,board,word,make_word,cur_x,cur_y,visited):
        if make_word==word:
            return True

        else:
            for i in range(4):
                nx=self.dx[i]+cur_x
                ny=self.dy[i]+cur_y
                if nx<0 or ny<0 or nx>=self.row or ny>=self.col or visited[nx][ny]:continue
                tmp_word=make_word+board[nx][ny]
                if tmp_word==word[:len(tmp_word)]:
                   visited[nx][ny] = True
                   flag=self.dfs(board,word,tmp_word,nx,ny,visited)
                   if flag:
                       return True
                   visited[nx][ny]=False


            return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row=len(board)
        self.col=len(board[0])
        visited=[False]*self.row
        for i in range(self.row):visited[i]=[False]*self.col

        for i in range(self.row):
            for j in range(self.col):
                tmp_word=board[i][j]
                if tmp_word==word[0]:
                    visited[i][j]=True
                    if self.dfs(board,word,tmp_word,i,j,visited):
                       return True

                    visited[i][j]=False


        return False








a=Solution()

a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")