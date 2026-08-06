class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Substring is longer than s2
        if len(s1) > len(s2):
            return False

        l = 0
        # Size of the window is length of s1.
        window_len = len(s1)
        r = window_len - 1

        # Fill up the dictionary.
        count_dict = {}
        for ch in s1:
            val = 1 + count_dict.get(ch, 0)
            count_dict[ch] = val

        # Go through the s2 in window of size len(s1)
        while l < (len(s2) - window_len + 1):
            subs2 = s2[l:r+1]

            # Find chars of subs2 present in count_dict
            tmp_count_dict = {}
            for ch in subs2:
                val = 1 + tmp_count_dict.get(ch, 0)
                tmp_count_dict[ch] = val
            
            all_matched = True
            for ch in subs2:
                s1_count = count_dict.get(ch, 0)
                sub_count = tmp_count_dict.get(ch, 0)
                
                # The ch in substr is not present in s1.
                if s1_count == 0:
                    all_matched = False
                    continue

                if s1_count != sub_count:
                    all_matched = False
                    break;

            if all_matched == True:
                return True
        
            l += 1
            r += 1

        return False
