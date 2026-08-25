class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int s, e, tmp_sum;
        vector<int> res;

        s = 1;
        e = numbers.size();
        tmp_sum = 0;

        while (s < e) {
            tmp_sum = numbers[s - 1] + numbers[e - 1];
            if (tmp_sum == target) {
                res.push_back(s);
                res.push_back(e);
                return res;
            } 
            else if (tmp_sum < target) {
                s++;
            } else {
                e--;
            }
        }

        return res;
    }
};
