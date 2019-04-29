
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        len_s = len(s)
        if s == 0 :
            return 0 
        i,j = 0 ,1
        max_len = 0
        while  i <=j and i <= len_s and j <= len_s:
            if len(set(s[i:j])) == len(s[i:j]):
                temp_len = j-i
                j += 1
                if temp_len > max_len:
                    max_len = temp_len
            else:
                i +=1
        return max_len

if __name__ == "__main__":
    s = Solution()
    s1 = " "
    res = s.lengthOfLongestSubstring(s1)
    print(res)

