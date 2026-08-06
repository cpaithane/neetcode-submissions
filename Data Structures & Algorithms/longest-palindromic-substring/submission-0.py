class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Start from middle and expand the string outside
        # of both the directions
        res = ""
        res_len = 0

        def form_palindrome(l, r):
            nonlocal res_len, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res_len = r - l + 1
                    res = s[l:r+1]
                    print("came here", l, r, res)

                l -= 1
                r += 1

        for i in range(0, len(s)):
            # Case of odd length palindromes
            l = i
            r = i
            form_palindrome(l, r)

            # Case of even length palindrome
            l = i
            r = i + 1
            form_palindrome(l, r)

        return res