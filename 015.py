class Solution:
    #时间复杂度较高，无法满足要求
    def threeSum(self,nums):
        nums_len = len(nums)
        if nums_len<3:
            return []
        res = []
        for i in range(nums_len-2):
            for j in range(i+1,nums_len-1):
                for k in range(j+1,nums_len):
                    temp =[nums[i],nums[j],nums[k]]
                    temp.sort()
                    if  temp not in res and sum(temp) == 0 :
                        res.append(temp)
        return list(res)
    def threeSum2(self,nums):
        nums_len = len(nums)
        if nums_len<3:
            return []
        res = []
        nums.sort()
        print(nums)
        for i in range(nums_len):
            if  i == 0 or nums[i]> nums[i-1]:
                l = i+1
                r = nums_len-1
                while l < r :
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0 :
                        res.append([nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l +=1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s <0:
                        l += 1
                    else:
                        r -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.threeSum2([-1,0,1,2,-1,-4])
    print(res)
