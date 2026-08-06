class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int missing_num = 0;

        for (int i = 0; i < nums.size(); i++) {
            missing_num = missing_num ^ nums[i];
        }
        return missing_num;
    }
};
