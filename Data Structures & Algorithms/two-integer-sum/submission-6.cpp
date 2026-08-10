class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        unordered_map<int, int> hash;

        for (int i = 0; i < nums.size(); i++) {
            hash.insert({nums[i], i});
        }

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (hash.find(diff) != hash.end() && hash[diff] != i) {
                if (i < hash[diff]) {
                    res.push_back(i);
                    res.push_back(hash[diff]);
                } else {
                    res.push_back(hash[diff]);
                    res.push_back(i);
                }
                
                break;
            }
        }

        return res;
    }
};
