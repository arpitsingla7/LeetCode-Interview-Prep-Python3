class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        wordMap = {"2": "abc", "3": "def", 
                   "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", 
                   "8": "tuv", "9": "wxyz"}
        res = []
        
        def backTrack(i, word):
            if len(word)==len(digits):
                res.append(word)
                return 
            curNum = digits[i]
            for ch in wordMap[curNum]:
                backTrack(i+1, word+ch)
            

        backTrack(0, "")
        return res
        
        