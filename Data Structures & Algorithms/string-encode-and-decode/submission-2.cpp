class Solution {
public:

    string encode(vector<string>& strs) {
        string res;

        for (string &s : strs) {
            res += to_string(s.size()) + "#" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> strs;

        for (int i = 0; i < s.size(); ) {
            int j = i;

            while (j < s.size() && s[j] != '#') {
                j++;
            }

            // i -> j is a size string.
            string len_str = s.substr(i, (j - i));
            int len = stoi(len_str);

            i = j + 1;
            strs.push_back(s.substr(i, len));
            i = i + len;
        }
        return strs;
    }
};
