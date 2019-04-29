class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        len_m = min(map(len,strs))
        i = 0
        while i < len_m:
            temp = strs[0][i]
            for j in range(len(strs)):
                if temp != strs[j][i] and i !=0:
                    return strs[0][:i]
                elif temp !=strs[j][i] :
                    return ''
            i +=1
        return strs[0][:len_m]

if __name__ == "__main__":
    s = Solution()
    arg =  []
    res = s.longestCommonPrefix(arg)
    print(res)