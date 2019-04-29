
#两数之和问题
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0 :
            return None
        for i in range(n):
            reminder = target - nums[i] 
            for j in range(i+1,n):
                if nums[j] == reminder:
                    return (i,j)
                    break
                