#https://leetcode.com/problems/max-area-of-island/ 
#695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.max_size=0
        self.current_size=0
        def isValid(row,col): 
            return 0<=row < m and 0<=col <n and grid[row][col] ==1
        
        def dfs(row,col):

            self.current_size +=1
            self.max_size =max(self.max_size,self.current_size)
            for dx,dy in directions:
                new_row,new_col =row+dx,col+dy
                if isValid(new_row,new_col) and (new_row,new_col) not in seen:
                    seen.add((new_row,new_col))
                    dfs(new_row,new_col)


        directions =[(0,1),(0,-1),(1,0),(-1,0)]
        seen =set()
        m=len(grid)
        n=len(grid[0])
        for row in range(m):
            for col in range(n):
                if (row,col) not in seen and grid[row][col] ==1:
                    seen.add((row,col))
                    self.current_size=0
                    dfs(row,col)
        return self.max_size
