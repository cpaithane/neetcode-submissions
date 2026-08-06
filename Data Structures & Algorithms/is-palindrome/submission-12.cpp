#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        int head = 0;
        int tail = s.size() - 1;
        
        while (head < tail) {
            /*
             * Traverse the string till first alpha-numeric char encounters.
             */
            while (head < tail && !isalnum(s[head])) {
                head++;
            }
            
            /*
             * Traverse the string backwards till first alpha-numeric char encounters.
             */
            while (tail > 0 && !isalnum(s[tail])) {
                tail--;
            }

            /*
             * A case where both pointers are crossed or at the same position.
             * E.g. "....."
             * E.g. "a."
             */
            if (head >= tail) {
                return true;
            }

            /*
             * Ignoring non-alpha numeric chars from both ends, the 
             * chars should match at both ends. If not, then string is
             * not palindrome.
             */
            if (toupper(s[head]) != toupper(s[tail])) {
                return false;
            }
            head++;
            tail--;
        }
        return true;
    }
};
