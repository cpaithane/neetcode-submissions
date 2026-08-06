class Solution:
    def palindrome(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        parts = []
        res_list = []

        def backtrack(i, parts):
            if i >= len(s):
                res_list.append(parts.copy())
                return

            for j in range(i, len(s)):
                if self.palindrome(s[i : j+1]):
                    parts.append(s[i : j+1])
                    backtrack(j + 1, parts)
                    parts.pop()

        backtrack(0, parts)
        return res_list