class Solution {
private:
    vector<string> res;
    string sub_res;
    unordered_map<char, vector<char>> dict_dig;

public:
    Solution() {
        dict_dig['2'] = {'a', 'b', 'c'};
        dict_dig['3'] = {'d', 'e', 'f'};
        dict_dig['4'] = {'g', 'h', 'i'};
        dict_dig['5'] = {'j', 'k', 'l'};
        dict_dig['6'] = {'m', 'n', 'o'};
        dict_dig['7'] = {'p', 'q', 'r', 's'};
        dict_dig['8'] = {'t', 'u', 'v'};
        dict_dig['9'] = {'w', 'x', 'y', 'z'};
    }

    void backtrack(int i, string &digits) {
        if (i == digits.size()) {
            res.push_back(sub_res);
            return;
        }

        if (i > digits.size()) {
            return;
        }

        vector<char> chars = dict_dig[digits[i]];
        for (char ch : chars) {
            sub_res.push_back(ch);
            backtrack(i + 1, digits);
            sub_res.pop_back(); 
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.size() > 0) {
            backtrack(0, digits);
        }
        return res;        
    }
};
