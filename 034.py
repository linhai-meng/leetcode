class Solution:
    def searchRange(self, nums, target):
        len_nums = len(nums)
        if len_nums == 0:
            return -1, -1
        left = self.searchleft(nums, 0, len_nums-1, target)
        right = self.searchRight(nums, 0, len_nums-1, target)
        return left, right

    def searchleft(self, nums, left, right, target):
        mid = (left+right) >> 1
        if left > right:
            return -1
        if (nums[mid] == target and mid == 0) or (mid > 0 and
                                                  nums[mid] == target and nums[mid-1] < target):
            return mid
        elif mid > 0 and (nums[mid] > target or (nums[mid] == nums[mid-1] and nums[mid] == target)):
            mid = self.searchleft(nums, left, mid-1, target)
        elif mid < right and nums[mid] < target:
            mid = self.searchleft(nums, mid+1, right, target)
        else:
            mid = -1
        return mid

    def searchRight(self, nums, left, right, target):

        mid = (left+right) >> 1
        if left > right:
            return -1
        if (nums[mid] == target and mid == right) or (mid < right
                                                      and nums[mid] == target and nums[mid+1] > target):
            return mid
        elif mid < right and (nums[mid] < target or (nums[mid] ==
                                                     nums[mid+1] and nums[mid] == target)):
            mid = self.searchRight(nums, mid+1, right, target)
        elif mid > 0 and nums[mid] > target:
            mid = self.searchRight(nums, left, mid - 1, target)
        else:
            mid = -1
        return mid


def searchRange(nums, target):
    # double pointer skill
    len_nums = len(nums)
    if len_nums == 0:
        return -1, -1
    left = 0
    right = len_nums - 1
    while left <= right:
        if nums[left] == target and nums[right] == target:
            return left, right
        if nums[left] < target:
            left += 1
        if nums[right] > target:
            right -= 1
    return -1, -1


if __name__ == '__main__':

    res = searchRange([5, 7, 7, 8, 8, 10], 0)
    print(res)
