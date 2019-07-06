
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    

    def climbStairs2(self,n) -> int:
        nums = [0 for i in range(n)]
        
        nums[0] = 1
        nums[1] = 2
        
        for i in range(2,len(nums)):
            nums[i] = nums[i-1] + nums[i-2]
        
        return nums[-1]