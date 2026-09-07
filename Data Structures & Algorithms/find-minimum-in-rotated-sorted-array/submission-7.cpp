class Solution {
public:
    int findMin(vector<int> &nums) {
        int s, e, res;

        s = 0, e = nums.size() - 1, res = nums[0];

        while (s <= e) {
            int m = (s + (e - s)/2);

            // arr between s and e is sorted.
            if (nums[s] < nums[e]) {
                res = min(res, nums[s]);
                break;
            }

            res = min(res, nums[m]);
            if (nums[s] <= nums[m]) {
                s = m + 1;
            } else {
                e = m -1;
            }
        }

        return res;
    }
};
