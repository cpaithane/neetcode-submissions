class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        min_res_len = float("inf")
        min_sub_str = ""
        count_dict = {}
        win_dict = {}
        have = 0

        # Build dictionary for t
        for ch in t:
            val = 1 + count_dict.get(ch, 0)
            count_dict[ch] = val

        need = len(count_dict)

        # Iterate through s
        for r in range(0, len(s)):
            ch = s[r]
            win_dict[ch] = 1 + win_dict.get(ch, 0)

            # If char is present in count_dict and count matches with that of t
            # As we are having ch from s, check if the char is present in count_dict.
            if ch in count_dict and win_dict[ch] == count_dict[ch]:
                have += 1

            while have == need:
                # Update the res string
                if (r - l + 1) < min_res_len:
                    min_res_len = r - l + 1
                    min_sub_str = s[l : r + 1]

                # Update have
                win_dict[s[l]] -= 1
                if s[l] in count_dict and win_dict[s[l]] < count_dict[s[l]]:
                    have -= 1

                # Shrink window by incrementing left
                l += 1

        return min_sub_str