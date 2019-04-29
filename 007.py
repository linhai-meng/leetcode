# 数字反转

class Solution:
    def reverse(self, x: int) -> int:
        symbol = 1
        if x < 0:
            symbol = -1
            x = symbol * x
        len_x = len(str(x))
        res = 0
        for i in range(len_x):
            num = 10 ** (len_x - 1 -i)
            num_remind = x %10
            x = x //10
            res += num_remind* num
        if symbol == 1 and res > 2**31-1:
            return 0
        elif symbol == -1 and res > 2** 31:
            return 0
        return symbol * res

if __name__ == "__main__":
    s = Solution()
    res = s.reverse(-98989899)
    print(res)

