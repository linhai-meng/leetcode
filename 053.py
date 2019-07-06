class Solution:
    def maxSubArray(self, nums) -> int:
        lenN= len(nums)
        for n in range(1,lenN):
            nums[n] = max(nums[n-1]+nums[n],nums[n])
            
            
        return max(nums)
    

if __name__ == '__main__':
    S = Solution()
    res = S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print('res is',res)
    