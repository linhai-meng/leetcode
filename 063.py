
# 回溯法解答方式
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        
        lenI = len(obstacleGrid)
        if lenI == 0:
            return 1
        if obstacleGrid[0][0] ==1:
            return 0
        lenJ = len(obstacleGrid[0])
        
        return self.count(obstacleGrid,lenI-1,lenJ-1,0,0)
    
    def count(self,ob,m,n,i,j):
        res = 0
        if i == m and j ==n and ob[m][n] !=1:
            return 1
        if i < m and ob[i+1][j] !=1:
            # ob[i+1][j] =1
            res += self.count(ob,m,n,i+1,j)
            
        if j < n and ob[i][j+1] != 1:
            # ob[i][j+1] = 1
            res += self.count(ob,m,n,i,j+1)

        return res
    
    
            

#回溯法的时间复杂度较高，利用动态规划法解答
class Solution1(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]
        
if __name__ == '__main__':
    S = Solution()
    # m = [ [0,0,0],[0,1,0],[0,0,0]]
    m = [[1,0]]
    res = S.uniquePathsWithObstacles(m)
    print('res is ',res)
    