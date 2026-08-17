class Solution {
public:

    bool alnum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }

    bool isPalindrome(string s) {
        int start = 0;
        int end = s.size() - 1;

        while (start < end) {
            while (start < end && !alnum(s[start])) {
                start += 1;
            }

            while (end > start && !alnum(s[end])) {
                end -= 1;
            }

            if (tolower(s[start]) != tolower(s[end])) {
                return false;
            }

            start += 1;
            end -= 1;
        }

        return true;
    }
};
