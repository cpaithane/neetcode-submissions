class Solution {
public:
    int search(vector<int>& nums, int target) {
        int s, e, res;

        s = 0, e = nums.size() - 1, res = -1;

        while (s <= e) {
            int m = (s + (e - s)/2);

            if (nums[m] == target) {
                res = m;
                break;
            }

            if (nums[s] <= nums[m]) {
                if (nums[s] <= target && nums[m] >= target) {
                    e = m;
                } else {
                    s = m + 1;
                }
            } else {
                if (nums[m] <= target && nums[e] >= target) {
                    s = m;
                } else {
                    e = m - 1;
                }
            }
        }

        return res;
    }
};
