class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> st;
        vector<int> res(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); i++) {
            int temp = temperatures[i];

            while (!st.empty() && temp > st.top().first) {
                auto [t, idx] = st.top();
                st.pop();
                res[idx] = i - idx;
            }

            st.push({temp, i});
        }

        return res;
    }
};
