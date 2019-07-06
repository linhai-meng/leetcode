class Solution:
    def maximalRectangle(self, matrix) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        heights = [0 for i in range(col)]
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] =="1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = self.largestRectangleArea(heights)
            maxArea = max(area,maxArea)
        return maxArea
        
    def largestRectangleArea(self, heights) -> int: 
        heights.append(0)
        stack = []
        stack.append(-1)
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1] !=-1 and heights[stack[-1]] >= heights[i]:
                maxArea = max(maxArea,heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return maxArea
    

if __name__ == '__main__':
    S = Solution()
    num = [ ["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"], ["1","0","0","1","0"]]

    res =S.maximalRectangle(num)
    print(res)
    