class Solution:
    def bfs(self,grid,row,col):
        if(row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or not grid[row][col]=='1'):
            return 
        grid[row][col]='0'
        self.bfs(grid,row+1,col)
        self.bfs(grid,row-1,col)
        self.bfs(grid,row,col+1)
        self.bfs(grid,row,col-1)
    def numIslands(self, grid: List[List[str]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    self.bfs(grid,i,j)
                    c=c+1
        return c
        