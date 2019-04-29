class Solution:
    def intToRoman(self, num: int) -> str:
        flag = 1
        if num < 0:
            flag = -1
        dev_num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        Roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res = ''
        for i , n in enumerate(dev_num):
            contain,remainder = self.nums(num,n)
            res += (contain* Roman[i])
            num = remainder
        return res
    def nums(self,num1,num2):
        contain = num1//num2
        remainder = num1 % num2
        return contain,remainder

if __name__ == "__main__":
    s= Solution()
    res = s.intToRoman(1994)
    print(res)
    