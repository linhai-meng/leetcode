

# 四数之和问题
# 难点
# 1. 确保不重复
# 2. 降低复杂度

class Solution:
    def fourSum(self, nums, target: int):
        len_nums = len(nums)
        if len_nums < 4:
            return []
        nums.sort()
        res = []
        for i in range(len_nums - 3):
            if (i==0 or nums[i]>nums[i-1]):
            # 使其相同的数字只计算一次
                for j in range(i+1, len_nums - 2):
                    if(j-i==1 or nums[j]>nums[j-1]):
                        remain = target - nums[i] - nums[j]
                        l, r = j + 1, len_nums - 1
                        while l < r:
                            
                            t = remain - nums[l] - nums[r]
                            if t == 0:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                                # 去除重复作用
                                l += 1
                                r -= 1
                                while l < r and nums[l] == nums[l-1]:
                                    l += 1
                                while l < r and nums[r] == nums[r+1]:
                                    r -= 1
                                
                            elif t < 0:
                                r -= 1
                            else:
                                l += 1
        return res
    def fourSum2(self, nums, target: int) :
            nums.sort()
            result = []
            for i in range(len(nums)-3):
                if (i==0 or nums[i]>nums[i-1]):
                    for j in range(i+1,len(nums)-2):
                        if(j-i==1 or nums[j]>nums[j-1]):
                                l = j+1
                                r = len(nums)-1
                                while l<r:
                                    if nums[i]+nums[j]+nums[r]+nums[l]==target:
                                        x = [nums[i],nums[j],nums[r],nums[l]]
                                        #if x not in result:
                                        result.append([nums[i],nums[j],nums[r],nums[l]])
                                        l = l+1
                                        r = r-1
                                        while l<r and nums[l]==nums[l-1]:
                                            l = l+1
                                        while l<r and nums[r]==nums[r+1]:
                                            r = r-1
                                    elif nums[i]+nums[j]+nums[r]+nums[l]>target:
                                        r = r-1
                                    else:
                                        l = l+1
            return result 

if __name__ == "__main__":
    s = Solution()
    arr = [1, 0, -1, 0, -2, 2]
    res = s.fourSum(arr, 0)
    print(res)
