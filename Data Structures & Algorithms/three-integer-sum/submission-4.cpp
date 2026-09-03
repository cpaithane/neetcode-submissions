class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {

            if (nums[i] > 0) {
                break;
            }

            // prev is same as that of cur, pair is already considered.
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int j = i + 1;
            int e = nums.size() - 1;

            while (j < e) {

                int target = (-1 * (nums[i] + nums[j]));

                if (target == nums[e]) {
                    vector<int> tmp_res = {nums[i], nums[j], nums[e]};
                    res.push_back(tmp_res);
                    j++, e--;

                    // prev is same as that of cur, pair is already considered.
                    while (nums[j] == nums[j - 1] && j < e) {
                        j++;
                    }
                } else if (target < nums[e]) {
                    e--;
                } else {
                    j++;
                }
            }
        }

        return res;
    }
};
