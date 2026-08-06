class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start = 0
        max_len = 0

        # Use sliding window algorithm.
        # start points to first char of the string and end points to last.
        # Check if s[end] is in hash. If it is there, increase the sliding window length
        # In every iteration update the max_len
        for end in range(0, len(s)):
            # While -> Because need to shrink the sliding window for duplicates.
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            
            charSet.add(s[end])
            max_len = max(max_len, (end - start + 1))
        
        return max_len