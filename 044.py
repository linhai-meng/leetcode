



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        
        ans = [[False for j in range(lenS+1)]for i in range(lenP+1)]
        ans[0][0] =True
        for i in range(1,lenP+1):
            for j in range(lenS+1):
                if p[i-1] == "*" and (ans[i-1][j]==1 or(j>0 and  ans[i][j-1]==1)):
                    ans[i][j] =True
                elif j>0 and ans[i-1][j-1] ==1 and (p[i-1] == s[j-1] or p[i-1] == "?"):
                    ans[i][j] =True
        
        return ans[lenP][lenS]
    

if __name__ == '__main__':
    S = Solution()
    s = "adceb"
    p = "*a*b"
    res = S.isMatch(s,p)
    print('result is ',res)
                    
                
