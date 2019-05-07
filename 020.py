class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 ==1:
            return False
        stack = []
        for i in s:

            if i =='(' or i == '{' or i == '[':
                stack.append(i)
            elif  len(stack) != 0 and ( (i == ')' and stack[-1] == '(') or \
                (i == ']' and stack[-1] == '[') or \
                (i== '}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    st = "}]}()){{)[{[(]"
    s = Solution()
    res = s.isValid(st)
    print(res)
            