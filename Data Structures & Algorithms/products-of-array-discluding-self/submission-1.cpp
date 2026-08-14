class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pre(nums.size());
        vector<int> suf(nums.size());
        vector<int> res(nums.size());
        int mult = 1;

        if (nums.size() == 0) {
            return res;
        }

        pre[0] = suf[nums.size() - 1] = 1;

        for (int i = 1; i < nums.size(); i++) {
            mult = mult * nums[i - 1];
            pre[i] = mult;
        }

        mult = 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            mult = mult * nums[i + 1];
            suf[i] = mult;
        }

        for (int i = 0; i < nums.size(); i++) {
            res[i] = pre[i] * suf[i];
        }

        return res;
    }
};
