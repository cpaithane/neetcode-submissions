class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        vector<int> res = {};

        /* Iterate through vector and insert number and index in hash. */
        for (int i = 0; i < nums.size(); i++) {
            hash[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            /* If difference is found in hash, return the vector. */
            auto it = hash.find(diff);
            if (it != hash.end() && it->second != i) {
                res.push_back(i);
                res.push_back(it->second);
                return res;
            }
        }
        return res;
    }
};
