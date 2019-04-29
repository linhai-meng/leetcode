
#正则表达式匹配

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_p ,len_s = len(p),len(s)
        res = [[False for j in range(len_p+1)] for i in range(len_s+1)]

        res[0][0] = True
        for i in range(len_p):
            if p[i] == '*' and res[0][i-1]:
                res[0][i+1] =True
        for i in range(len_s):
            for j in range(len_p):
                if p[j] == '*':
                    if p[j-1] !=s[i] and p[j-1] != '.':
                        res[i+1][j+1] = res[i+1][j-1]
                    else:
                        res[i+1][j+1] = res[i+1][j] or res[i][j+1] or res[i+1][j-1]
                elif p[j] =='.' or p[j] == s[i]:
                    res[i+1][j+1] = res[i][j]
                    
        return res[len_s][len_p]

if __name__ == "__main__":
    s = Solution()
    res = s.isMatch('aab','c*a*b')
    print(res)