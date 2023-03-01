class Solution(object):
    def letterCombinations(self, digits):
        res = []
        DtoL = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtracking(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return 
            for c in DtoL[digits[i]]:
                backtracking(i + 1, curStr + c)

        if digits:
            backtracking(0, "")

        return res

if __name__ == '__main__':
    digits = input()
    print(Solution.letterCombinations(Solution, digits))