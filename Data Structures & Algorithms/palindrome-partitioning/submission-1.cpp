class Solution {
private:
    vector<vector<string>> res_list;
    vector<string> sub_res;

    bool palindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }

public:
    void backtrack(int i, string s) {
        if (i >= s.size()) {
            res_list.push_back(sub_res);
            return;
        }

        for (int j = i; j < s.size(); j++) {
            if (palindrome(s.substr(i, j - i + 1))) {
                sub_res.push_back(s.substr(i, j - i + 1));
                backtrack(j + 1, s);
                sub_res.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        backtrack(0, s);
        return res_list;
    }
};
