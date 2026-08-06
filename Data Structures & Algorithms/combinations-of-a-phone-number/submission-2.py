class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_dig = {}
        dict_dig['2'] = ['A', 'B', 'C']
        dict_dig['3'] = ['D', 'E', 'F']
        dict_dig['4'] = ['G', 'H', 'I']
        dict_dig['5'] = ['J', 'K', 'L']
        dict_dig['6'] = ['M', 'N', 'O']
        dict_dig['7'] = ['P', 'Q', 'R', 'S']
        dict_dig['8'] = ['T', 'U', 'V']
        dict_dig['9'] = ['W', 'X', 'Y', 'Z']

        res_list = []
        res = ""

        def backtrack(i, res):
            # Base conditions
            if len(res) == len(digits):
                res_list.append(res.lower())
                return

            if i > len(digits):
                return

            for ch in dict_dig[digits[i]]:
                backtrack(i+1, res + ch)

        if len(digits) > 0:
            backtrack(0, res)
        
        return res_list