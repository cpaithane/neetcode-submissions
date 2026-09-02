class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len = digits.size();
        int carry, total;
        vector<int> res;
        carry = total = 0;

        for (int i = len - 1; i >= 0; i--) {
            if (i == len - 1) {
                total = carry + digits[i] + 1;
            } else {
                total = carry + digits[i];
            }

            carry = total / 10;
            res.push_back(total % 10);
        }

        if (total >= 10) {
            res.push_back(total / 10);
        }

        reverse(res.begin(), res.end());
        return res;
    }
};
