class Solution:
    def largestRectangleArea(self, heights):
   
        heights.append(0)
        st, mx = [], 0
        for i in range(len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                c = st.pop()
                mx = max(mx, heights[c]*(i-st[-1]-1 if st else i))
            st.append(i)
        return mx
    def largestRectangleArea2(self,height):
        
        height.append(0)
        stack = []
        stack.append(-1)
        maxArea = 0
        for i in range(len(height)):
            while stack[-1] !=-1 and height[stack[-1]] >= height[i]:
                maxArea = max(maxArea,height[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        
        return maxArea
    

if __name__ == '__main__':
    S = Solution()
    res = S.largestRectangleArea2([2,1,5,6,2,3])
    print(res)
    