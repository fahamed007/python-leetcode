#https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150
#130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(row,col):
            return  0<=row<m and 0<=col<n and board[row][col] =="O"
        
        def dfs(row,col):
            for dx,dy in directions:
                new_row,new_col =row+dx,col+dy
                if is_valid(new_row,new_col) and (new_row,new_col) not in seen:
                    seen.add((new_row,new_col))
                    board[new_row][new_col] ="E"
                    dfs(new_row,new_col)

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(board)
        n=len(board[0])
        seen=set()

        for row in [0,m-1]:
            for col in range(n):
                if board[row][col] =="O" and (row,col) not in seen:
                    seen.add((row,col))
                    board[row][col] ="E"
                    dfs(row,col)

        for col in [0,n-1]:
            for row in range(m):
                if board[row][col] =="O" and (row,col) not in seen:
                    seen.add((row,col))
                    board[row][col] ="E"
                    dfs(row,col)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] =="O":
                    board[row][col] ="X"
                elif board[row][col] =="E":
                    board[row][col] ="O"






        
