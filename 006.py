
# z自行变换

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        len_s = len(s)
        row = min(numRows,len_s)

        arr = [[] for i in range(row)]

        row_num = 0
        operate = 1
        for i in range(len_s):
            arr[row_num].append(s[i])
            row_num += operate
            if row_num == 0 or row_num == numRows -1:
                operate *=-1
        res = ''
        print(arr)
        for i in arr:
            res +=''.join(i)
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.convert('LEETCODEISHIRING',4)
    print(res)