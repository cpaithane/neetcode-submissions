class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;

        while (start <= end) {
            /* To avoid the integer overflow. */
            int mid = start + (end - start) / 2;

            /* The target matched in the array. */
            if (nums[mid] == target) {
                return mid;
            }

            /* The target is in the right part of the array. */
            if (nums[mid] < target) {
                start = mid + 1;
            } else {
                /* The target is in the left part of the array. */
                end = mid - 1;
            }
        }
        return -1;
    }
};
