
# 三数最接近的数


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        len_nums = len(nums)
        if len_nums <= 3:
            return sum(nums)
        nums.sort()
        min_d = nums[0] + nums[1] + nums[2] - target
        for n in range(len(nums)-2):
            l = n + 1
            r = len(nums) - 1
            while l < r:
                temp = nums[n]+nums[l]+nums[r] - target
                if abs(min_d) > abs(temp):
                    min_d = temp
                if temp == 0:
                    break
                if temp < 0:
                    l += 1
                elif temp > 0:
                    r -= 1
        return min_d + target


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,1]
    res = s.threeSumClosest(nums, 3)
    print(res)
