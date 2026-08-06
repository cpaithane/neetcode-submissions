#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        int head = 0;
        int tail = s.size() - 1;
        
        while (head < tail) {
            while (!isalnum(s[head])) {
                head++;
            }
            
            while (!isalnum(s[tail])) {
                tail--;
            }

            if (head >= tail) {
                return true;
            }

            if (toupper(s[head]) != toupper(s[tail])) {
                return false;
            }
            head++;
            tail--;
        }
        return true;
    }
};
