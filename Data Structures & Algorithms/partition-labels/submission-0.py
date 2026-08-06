class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res_list = []
        char_dict = {}
        for i in range(0, len(s)):
            ch = s[i]
            char_dict[ch] = i

        i = last_idx = start = end = 0

        while i < len(s):
            ch = s[i]
            last_idx = char_dict[ch]
            end = max(end, last_idx)
            
            if i == end:
                res_list.append(end - start + 1)
                start = i + 1

            i += 1

        return res_list