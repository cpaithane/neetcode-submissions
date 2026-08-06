class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool found = false;

        if (nums.size() == 0) {
            return found;
        }

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 1; i++) {
                if (nums[i] == nums[i + 1]) {
                    found = true;
                    break;
                }
        }
        return found;
    }
};