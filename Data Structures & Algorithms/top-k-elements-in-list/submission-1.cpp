class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<int> res;

        for (int num : nums) {
            count[num] += 1;
        }

        /* Creating bucket based on frequency of numbers. */
        vector<vector<int>> freq(nums.size() + 1);
        for (auto [n, f] : count) {
            freq[f].push_back(n);
        }

        for (int i = freq.size() - 1; i > 0; i--) {
            for (int num : freq[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};
