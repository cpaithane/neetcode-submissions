class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        l = 0
        max_freq = 0
        res = 0

        #
        # window_len - most_freq_char is the no. of chars to be replaced.
        # E.g. AAABA => W_len = 5, freq_max = 4 (freq of A) (5 - 4) = 1
        # 1 char can be replaced.
        #

        # Go through string s.
        # l points to 0, r points to 0 initially.
        # len_window = 1
        for r in range(len(s)):
            # Find out freq of s[r] and max_freq char in the window
            freq = 1 + count_dict.get(s[r], 0)
            count_dict[s[r]] = freq
            max_freq = max(freq, max_freq)

            #
            # Shrink the sliding window when no. of  chars to replace with exceeds k
            #
            while (r - l + 1) - max_freq > k:
                count_dict[s[l]] -= 1
                l += 1
                
            # Calculate res in this iteration
            res = max((r - l + 1), res)

        return res
        