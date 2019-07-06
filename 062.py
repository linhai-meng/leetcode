
# different path

class Solution:
    def uniquePaths(self,m,n) -> int:
        
        if m==1 or n ==1 :
            return 1
        if m < n:
            m, n = n , m
        top =1
        down = 1
        for i in range(1,n):
            top = top * (m+i-1)
            down = down * i
        return (top//down)
    

if __name__ == '__main__':
    S = Solution()
    res = S.uniquePaths(7,3)
    print('res is',res)
    
        
    