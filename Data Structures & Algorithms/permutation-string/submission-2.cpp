class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        
        if (s1.size() > s2.size()) {
            return false;
        }

        int l, window_len, r;
        unordered_map<char, int> main_map;

        for (char ch : s1) {
            main_map[ch] = 1 + main_map[ch];
        }

        l = 0;
        window_len = s1.size();
        r = window_len - 1;

        while (l < (s2.size() - window_len + 1)) {
            string sub_s2 = s2.substr(l, (r - l + 1));

            unordered_map<char, int> tmp_map;
            for (char ch : sub_s2) {
                tmp_map[ch] = 1 + tmp_map[ch];
            }

            bool all_matched = true;
            for (char ch : sub_s2) {
                int s1_count = main_map[ch];
                int sub_count = tmp_map[ch];

                if (s1_count == 0) {
                    all_matched = false;
                    continue;
                }

                if (s1_count != sub_count) {
                    all_matched = false;
                    break;
                }
            }

            if (all_matched) {
                return true;
            }

            l++;
            r++;
        }

        return false;
    }
};
