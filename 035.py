class Solution:
    def searchInsert(self, nums, target: int) -> int:
        len_nums = len(nums)
        if len_nums ==0 or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len_nums
        left ,right = 0 , len_nums-1
        while left <= right:
            mid = (left+right)>>1
            if (nums[mid] == target) or (mid > 0 and nums[mid-1] < target and nums[mid] > target):
                return mid
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
                
                
if __name__ == '__main__':
    S = Solution()
    res = S.searchInsert([1,3], 2)
    print(res)
    