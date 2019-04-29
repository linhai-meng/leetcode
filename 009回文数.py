class Solution:
    def isPalindrome(self, x: int) -> bool:
        if   x ==None:
            return False
        if x <0:
            return False
        str_x = str(x)
        n = len(str_x)
        if n == 0:
            return False
        left,right = 0,n-1
        while left <=right:
            if str_x[left] == str_x[right]:
                left +=1
                right -=1
            else:
                return False
        return True

if __name__ == "__main__":
    s= Solution()
    res = s.isPalindrome(0)
    print(res)