class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP - Topdown in O(m*n)
        len_s = len(s)
        len_p = len(p)
        dp = {}

        def recurse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            # Base condition
            if j == len_p and i == len_s:
                return True

            if j >= len_p:
                return False

            match = i < len_s  and (s[i] == p[j] or p[j] == ".")

            # If next char in p is *, either move p by 2 or s by 1.
            if (j + 1 < len_p) and p[j + 1] == "*":
                dp[(i, j)] = (recurse(i, j + 2) or (match and recurse(i + 1, j)))
                return dp[(i, j)]

            # If chars match in s and p or p has ., then
            # move s and p both by 1
            if match:
                dp[(i, j)] = recurse(i + 1, j + 1)
                return dp[(i, j)]
            
            # Chars mismatch, return False
            dp[(i, j)] = False
            return False

        return recurse(0, 0)      

        # Recursive O(2^n)
        len_s = len(s)
        len_p = len(p)

        def recurse(i, j):
            # Base condition
            if j == len_p and i == len_s:
                return True

            if j >= len_p:
                return False

            match = i < len_s  and (s[i] == p[j] or p[j] == ".")

            # If next char in p is *, either move p by 2 or s by 1.
            if (j + 1 < len_p) and p[j + 1] == "*":
                return (recurse(i, j + 2) or (match and recurse(i + 1, j)))

            # If chars match in s and p or p has ., then
            # move s and p both by 1
            if match:
                return recurse(i + 1, j + 1)
            
            # Chars mismatch, return False
            return False

        return recurse(0, 0)