class Solution {
    int pre, suf, res;

    int multiply(int num, int multiplier) {
        if (multiplier == 0) {
            multiplier = 1;
        }
        return num * multiplier;
    }

public:
    int maxProduct(vector<int>& nums) {
        suf = pre = 0;
        res = nums[0];

        for (int i = 0; i < nums.size(); i++) {
            pre = multiply(nums[i], pre);
            suf = multiply(nums[nums.size() - i - 1], suf);
            res = max(res, max(pre, suf));
        }

        return res;
    }
};
