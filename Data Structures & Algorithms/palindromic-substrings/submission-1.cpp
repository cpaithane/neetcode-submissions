class Solution {
private:
    int nr_palin;

    void find_palindrome(int l, int r, string &s) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            nr_palin++;
            l--;
            r++;
        }
    }

public:
    int countSubstrings(string s) {
        nr_palin = 0;

        for (int i = 0; i < s.size(); i++) {
            int l = i;
            int r = i;
            find_palindrome(l, r, s);
        }

        for (int i = 0; i < s.size(); i++) {
            int l = i;
            int r = i + 1;
            find_palindrome(l, r, s);
        }

        return nr_palin;
    }
};
