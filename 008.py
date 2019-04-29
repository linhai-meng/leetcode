class Solution:
    def myAtoi(self, s: str) -> int:
        operate = 1
        nums = set([str(i) for i in range(10)])
        s = s.strip()
        if len(s) == 0:
            return 0
        if (s[0] != '-' and s[0] != '+' )and s[0] not in nums:
            return 0 
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            operate = -1
            s = s[1:]
        res = []
        i = 0
        while i < len(s) and s[i] in nums:
            res.append(s[i])
            i+=1
        if len(res) ==0:
            return 0
        res_num = int(''.join(res))
        if operate == -1 and res_num > 2**31:
            return operate* 2**31
        elif operate == 1 and res_num > 2 **31 -1:
            return 2**31-1
        return operate * res_num


if __name__ == "__main__":
    s = Solution()
    res = s.myAtoi('+1')
    print(res)