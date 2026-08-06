#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        int head = 0;
        int tail = s.size() - 1;
        
        while (head < tail) {
            while (head < tail && !isalnum(s[head])) {
                head++;
            }
            
            while (tail > 0 && !isalnum(s[tail])) {
                tail--;
            }

            if (head >= tail) {
                return true;
            }
            cout << "head " << head;
            cout << "tail " << tail;
            cout << endl;

            if (toupper(s[head]) != toupper(s[tail])) {
                return false;
            }
            head++;
            tail--;
        }
        return true;
    }
};
