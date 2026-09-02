class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int x_or = 0;

        for (int i = 0; i <= n; i++) {
            x_or = x_or ^ i;
        }

        for (int &num : nums) {
            x_or = x_or ^ num;
        }

        return x_or;
    }
};
