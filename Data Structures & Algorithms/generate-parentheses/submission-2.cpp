class Solution {
private:
    vector<string> res;
    string st;

public:
    void recurse(int o, int c, int n) {
        if ((o == n) && (c == n)) {
            res.push_back(st);
            return;
        }

        if (o < n) {
            st.push_back('(');
            recurse(o + 1, c, n);
            st.pop_back();
        }

        if (c < o) {
            st.push_back(')');
            recurse(o, c + 1, n);
            st.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        recurse(0, 0, n);
        return res;        
    }
};
