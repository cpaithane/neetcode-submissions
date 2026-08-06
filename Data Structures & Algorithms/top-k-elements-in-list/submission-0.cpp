class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        unordered_map<int, int> count;

        for (int num : nums) {
            count[num] = 1 + count[num];
        }

        vector<vector<int>> freq(nums.size() + 1);
        for (auto entry : count) {
            freq[entry.second].push_back(entry.first);
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
