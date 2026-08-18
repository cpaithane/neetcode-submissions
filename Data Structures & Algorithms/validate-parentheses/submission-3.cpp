class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> close_map = {{')', '('},
                                               {']', '['},
                                               {'}', '{'}};

        stack<char> st;

        for (char &ch : s) {
            if (close_map.count(ch)) {
                if (!st.empty() && st.top() == close_map[ch]) {
                    st.pop();
                } else {
                    return false;
                }
            } else {
                st.push(ch);
            }
        }

        return st.empty();
    }
};
