class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> st;

        for (string &token : tokens) {
            // operators
            if (token == "+" || token == "-" ||
                token == "*" || token == "/") {
                string num1 = st.top();
                st.pop();
                string num2 = st.top();
                st.pop();

                int i_res, i_num1, i_num2;
                i_num2 = stoi(num1);
                i_num1 = stoi(num2);
                i_res = 0;

                if (token == "+") {
                    i_res = i_num1 + i_num2;
                } else if (token == "-") {
                    i_res = i_num1 - i_num2;
                } else if (token == "*") {
                    i_res = i_num1 * i_num2;
                } else {
                    i_res = i_num1 / i_num2;
                }

                st.push(to_string(i_res));
            } else {
                st.push(token);
            }
        }
        return stoi(st.top());
    }
};
