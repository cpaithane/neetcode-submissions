class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP
        dp = {}

        def core(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = core(i + 1, j, k + 1)

            if not res and j < len(s2) and s2[j] == s3[k]:
                res = core(i, j + 1, k + 1)

            dp[(i, j)] = res
            return res

        return core(0, 0, 0)

        # Recursive
        #
        # Start from 0 of all the strings
        # If char in s3 matches s1, go for next in s1
        # If char in s3 matches s2, go for next in s2
        # If k reaches len(s3), then check if i and j has reached their
        # end of the strings.
        #
        def core(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[k]:
                if core(i + 1, j, k + 1):
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if core(i, j + 1, k + 1):
                    return True

            # n - m goes beyond 1
            return False

        return core(0, 0, 0)