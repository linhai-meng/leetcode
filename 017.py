class Solution:
    def letterCombinations(self, digits: str):
        self.num2str = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],\
            '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res = []
        self.letterSolution(digits,0,res)
        return res

    def letterSolution(self,digits,index,res):
        if index >= len(digits):
            return []
        ch = digits[index]
        mapping = self.num2str[ch]
        print(mapping)
        if len(res) == 0:
            for i in mapping:
                res.append(i)
        else:
            length = len(res)
            for i in mapping:
                for j in range(length):
                    res.append(res[j]+i)
            for j in range(length):
                res.pop(0)

                # print('res ',res)
                # print('index',index)
                # temp = self.letterSolution(digits,index+1,res)
        self.letterSolution(digits,index+1,res)

if __name__ == "__main__":
    s = Solution()
    res = s.letterCombinations('23')
    print(res)
