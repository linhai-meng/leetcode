class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        if height == None:
            return 0
        len_h = len(height)
        if len_h <=1:
            return 0 
        left,right = 0 , len_h -1
        min_h_pre = 0
        flag = True
        while left < right:
            if   height[left] <= height[right] and height[left] <= min_h_pre:
                left +=1
            if  height[right] < height[left] and height[right] <= min_h_pre:
                right -=1
            min_h_pre = min(height[left],height[right])
            area  = (right - left)*min_h_pre
            if area > max_area:
                max_area = area
        return max_area
if __name__ == "__main__":
    s = Solution()
    l = [11,11,11]
    res = s.maxArea(l)
    print(res)
   