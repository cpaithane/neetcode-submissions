class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        unordered_map<int, int> hash;

        for (int i = 0; i < nums.size(); i++) {
            hash[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (hash.find(diff) != hash.end() && hash[diff] != i) {
                res.push_back(i);
                res.push_back(hash[diff]);
                break;
            }
        }

        return res;
    }
};
