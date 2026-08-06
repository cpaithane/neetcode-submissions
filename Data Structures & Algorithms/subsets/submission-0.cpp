class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        /* Empty set */
        vector<vector<int>> res = {{}};

        /* For every member in input vector.*/
        for (int num : nums) {
            int size = res.size();

            /*
             * For every vector in res, create cur_subset by
             * inserting num. Push the cur_subset in res.
             */
            for (int i = 0; i < size; i++) {
                vector<int> cur_subset = res[i];
                cur_subset.push_back(num);
                res.push_back(cur_subset);
            }
        }
        return res;
    }
};
