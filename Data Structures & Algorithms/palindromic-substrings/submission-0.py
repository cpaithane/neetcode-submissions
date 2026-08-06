class Solution:
    def countSubstrings(self, s: str) -> int:
        nr_palin = 0

        def find_palindrome(l, r):
            nonlocal nr_palin
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nr_palin += 1
                l -= 1
                r += 1

        for i in range(0, len(s)):
            l = i
            r = i
            find_palindrome(l, r)

            l = i
            r = i + 1
            find_palindrome(l, r)

        return nr_palin