class Solution {
private:
    string res;
    int res_len;

    void form_palindrome(int l, int r, string &s) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            if (res_len < (r - l + 1)) {
                res_len = (r - l + 1);
                res = s.substr(l, (r - l + 1));
            }
            l--;
            r++;
        }
    }

public:
    string longestPalindrome(string s) {
        res = "";
        res_len = 0;

        for (int i = 0; i < s.size(); i++) {
            int l = i;
            int r = i;
            form_palindrome(l, r, s);
        }

        for (int i = 0; i < s.size(); i++) {
            int l = i;
            int r = i + 1;
            form_palindrome(l, r, s);
        }

        return res;
    }
};
