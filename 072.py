
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        
        ans = [[0 for j in range(lenWord2+1)] for i in range(lenWord1+1)]
        
        for i in range(lenWord1+1):
            ans[i][0] = i
        
        for i in range(lenWord2+1):
            ans[0][i] = i
        
        for i in range(1,lenWord1+1):
            for j in range(1,lenWord2+1):
                if word1[i-1] == word2[j-1]:
                    ans[i][j] = ans[i-1][j-1]
                else:
                    ans[i][j] = min(ans[i-1][j],ans[i][j-1],ans[i-1][j-1])+1
        return ans[lenWord1][lenWord2]
    
if __name__ == '__main__':
    s = Solution()
    res = s.minDistance("zoologicoarchaeologist", "zoogeologist")
    print('res is',res)
    