class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1:
            return ''
        start = 0
        end = 0
        for i in range(len(s)):
            l = self.longest(s,i,i)
            r = self.longest(s,i,i+1)
            len_m = max(l,r)
            if len_m > end-start:
                start = i - (len_m-1)//2
                end = i+ len_m//2
        return s[start:end+1]

    def longest(self,s,left,right):
        len_s = len(s)
        while left >= 0 and right < len_s and s[left] == s[right]:
            left -=1
            right +=1
        return right - left - 1
if __name__ == "__main__":
    s = Solution()
    res = s.longestPalindrome('aaabaaadfadfdsfadsfsdfsd')
    print(res)

                


