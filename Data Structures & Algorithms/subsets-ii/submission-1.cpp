class Solution {
private:
    vector<vector<int>> res_list;
    vector<int> sub_res;

public:
    void recurse(int i, vector<int>& nums) {
        if (i == nums.size()) {
            res_list.push_back(sub_res);
            return;
        }

        sub_res.push_back(nums[i]);
        recurse(i + 1, nums);

        sub_res.pop_back();

        while ((i + 1 < nums.size()) && (nums[i] == nums[i + 1])) {
            i++;
        }
        recurse(i + 1, nums);
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());        
        recurse(0, nums);
        return res_list;
    }
};
