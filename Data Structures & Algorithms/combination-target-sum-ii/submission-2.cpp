class Solution {
private:
    vector<vector<int>> res_list;

public:
    void recurse(vector<int> &candidates, int sum, int i, vector<int> sub_res, int target) {
        if (sum == target) {
            res_list.push_back(sub_res);
            return;
        }

        if (i >= candidates.size() || sum > target) {
            return;
        }

        sub_res.push_back(candidates[i]);
        recurse(candidates, sum + candidates[i], i + 1, sub_res, target);
        sub_res.pop_back();

        while (((i + 1) < candidates.size()) && (candidates[i] == candidates[i + 1])) {
            i++;
        }

        recurse(candidates, sum, i + 1, sub_res, target);
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> sub_res;
        sort(candidates.begin(), candidates.end());
        recurse(candidates, 0, 0, sub_res, target);        
        return res_list;
    }
};
