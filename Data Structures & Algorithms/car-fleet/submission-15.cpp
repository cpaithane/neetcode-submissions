class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pairs;
        vector<double> st;

        for (int i = 0; i < position.size(); i++) {
            pairs.push_back({position[i], speed[i]});
        }

        sort(pairs.rbegin(), pairs.rend());

        for (auto [p, s] : pairs) {
            st.push_back(((double) (target - p)/s));

            /*
             * two cars will form a fleet if and only if the car ahead
             * has a time that is greater than or equal to the time of
             * the car behind it
             */
            if (st.size() >= 2 &&
                st.back() <= st[st.size() - 2]) {
                st.pop_back();
            }
        }

        return st.size();
    }
};
