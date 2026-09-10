class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int i = 0;

        while (i < nums.size()) {
            int num = nums[i];

            if (i == (num - 1)) {
                i++;
                continue;
            }

            if (num == nums[nums[i] - 1]) {
                return num;
            }

            int tmp = num;
            nums[i] = nums[num - 1];
            nums[num - 1] = tmp;
        }

        return -1;
    }
};
