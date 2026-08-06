class Solution {
public:
    string encode(vector<string>& strs) {
        string enc_str;

        for (string s : strs) {
            enc_str += to_string(s.size()) + "#" + s;
        }
        return enc_str;
    }

    vector<string> decode(string s) {
        vector<string> strs;

        for (int i = 0; i < s.size();) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }

            /* length of the string can be found from i to j */
            string len_str = s.substr(i, (j-i));
            int length = stoi(len_str);

            i = j + 1;
            j = i + length;
            strs.push_back(s.substr(i, length));
            i = j;
        }
        return strs;
    }
};
