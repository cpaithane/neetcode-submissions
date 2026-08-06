class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set()
        start_seqs = []

        for num in nums:
            seq.add(num)

        for num in nums:
            if (num - 1) not in seq:
                start_seqs.append(num)

        max_len = 0
        for start_seq in start_seqs:
            seq_len = 0
            for i in range(start_seq, len(nums)+1):
                if i in seq:
                    seq_len += 1
                else:
                    break
            
            if seq_len > max_len:
                max_len = seq_len
        
        return max_len
