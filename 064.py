
class Solution:
    def minPathSum(self, grid) -> int:
        
        R = len(grid)
        if R > 0:
            L = len(grid[0])
        
        for i in range(1,L):
            grid[0][i] += grid[0][i-1]
        
        for j in range(1,R):
            grid[j][0] += grid[j-1][0]
        
        for i in range(1,R):
            for j in range(1,L):
                grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]
        
        return grid[R-1][L-1] 
    
if __name__ == '__main__':
    S = Solution()
    arr = [[1,3,1],[1,5,1],[4,2,1]]
    res = S.minPathSum(arr)
    print('res is',res)
    