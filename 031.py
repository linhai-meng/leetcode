
class Solution:
    def nextPermutation(self, nums):
        len_nums = len(nums)
        if len_nums <= 1:
            return nums

        for i in range(len_nums-1):
            if nums[len_nums-i-2] < nums[len_nums-i-1]:

                nums[(len_nums-i-2):] = sorted(nums[(len_nums-i-2):])

                nums[len_nums-i-2], nums[len_nums-i -
                                         1] = nums[len_nums-i-1], nums[len_nums-i-2]

        return nums.sort()

    def nextPermutation2(self, nums):
        n = len(nums) - 1
        tmp = n
        record = []
        while n > 0:
            if nums[n] > nums[n - 1]:
                k = 0
                record.append(nums[n])
                min_val = record[k]
                while min_val <= nums[n - 1]:
                    k += 1
                    min_val = record[k]
                index = tmp - k
                nums[n - 1], nums[index] = nums[index], nums[n - 1]
                nums[n:] = nums[n:][::-1]
                return
            else:
                record.append(nums[n])
                n -= 1
        return nums.reverse()

    def nextPermutation3(self, nums):
    


        def reverse(nums, start):
            i, j = start, len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = len(nums)-2
        # 1. 找出是否有前一个小于后一个情况
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            # 2. 找出刚好大于i的j位置值
            while j >= 0 and nums[j] <= nums[i]:
                print(j)
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 3. 最后对后面的排序
        reverse(nums, i+1)
        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.nextPermutation3([4, 5, 3, 2, 1])
