class Solution {
public:
    string calc_hash(string &str) {
        vector<int> count(26, 0);

        for (char &ch : str) {
            count[ch - 'a']++;
        }

        string key = to_string(count[0]);
        for (int i = 0; i < 26; i++) {
            key += ":" + to_string(count[i]);
        }
        return key;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> groups;
        unordered_map<string, vector<string>> hash;

        for (string &s : strs) {
            hash[calc_hash(s)].push_back(s);
        }

        for (auto [k, v] : hash) {
            groups.push_back(v);
        }

        return groups;
    }
};
