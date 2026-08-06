#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        int size = s.size();
        if (size == 0) {
            return true;
        }
        if (size % 2 == 1) {
            return false;
        }
        cout << "string = " << s << endl;
        for (char ch : s) {
            cout << "char = " << ch << endl;
            /* If opening bracket, push to stack. */
            if (ch == '(' ||
                ch == '{' ||
                ch == '[') {
                st.push(ch);
            } else if (st.empty()) {
                /*
                 * If string is not exhausted and stack is empty, then invalid char.
                 */
                return false;
            } else {
                /* Else, pop and match. */
                char popped_char = st.top();
                st.pop();
                if (popped_char == '(' && ch != ')' ||
                    popped_char == '{' && ch != '}' ||
                    popped_char == '[' && ch != ']') {
                    return false;
                }
            }
        }
        return st.empty();
    }
};
