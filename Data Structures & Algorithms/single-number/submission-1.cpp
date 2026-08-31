class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int missing = 0;

        for (int &num : nums) {
            missing = missing ^ num;
        }

        return missing;
    }
};
