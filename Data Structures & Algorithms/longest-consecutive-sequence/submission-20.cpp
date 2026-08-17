class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seq;
        int max_len = 0;
        int seq_len = 0;

        // Build sequence.
        for (int &num : nums) {
            seq.insert(num);
        }

        // Build start_seq
        for (int &num : nums) {
            if (seq.find(num - 1) == seq.end()) {
                seq_len = 1;

                while (seq.find(num + seq_len) != seq.end()) {
                    seq_len++;
                }

                if (seq_len > max_len) {
                    max_len = seq_len;
                }

            }
        }
        
        return max_len;
    }
};
