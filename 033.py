
def search(nums, target):

    len_nums = len(nums)
    if len_nums == 0:
        return -1
    elif len_nums == 1 and nums[0] == target:
        return 0

    left = 0
    right = len_nums - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] - target == 0:
            return mid
        elif nums[mid] < nums[right]:
            if target > nums[mid] and target <= nums[right]:
                left = mid+1
            else:
                right = mid - 1
        elif nums[mid] > nums[left]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


class Solution:
    def search(self, nums, target):
        """搜索排序螺旋数组"""
        def half_search(nums, target, l, r):
            """二分查找"""
            mid = (l + r) // 2
            if l>r:return -1
            if nums[mid] == target:return mid

            # 三种情况向前查找
            # 0-mid无旋转 o-mid包含旋转 target在0-旋转位置之间
            if (nums[0]<=target<=nums[mid]) or (target<=nums[mid]<nums[0]) or (nums[mid]<nums[0]<=target):
                return half_search(nums, target, l, mid-1)
            else:
                return half_search(nums, target, mid+1, r)

        if not nums:return -1
        return half_search(nums, target, 0, len(nums)-1)
    
    
    
    
    
if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]

    res = search(nums, 0)
    print(res)
