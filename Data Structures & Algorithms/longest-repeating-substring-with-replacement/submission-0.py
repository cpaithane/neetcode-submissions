class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            freq = 1 + count_dict.get(s[r], 0)
            count_dict[s[r]] = freq
            max_freq = max(freq, max_freq)

            while (r - l + 1) - max_freq > k:
                count_dict[s[l]] -= 1
                l += 1
                
            res = max((r - l + 1), res)

        return res
        