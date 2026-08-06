class Solution {
public:

    /*
     * Calculate key. Take vector of count for every char of string.
     * Convert the vector in string and use it as key.
     */
    string calc_key(string s) {
        vector<int> count(26, 0);

        for (char ch : s) {
            count[ch - 'a']++;
        }

        string key = to_string(count[0]);
        for (int i = 1; i < 26; i++) {
            key += ":" + to_string(count[i]);
        }

        return key;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash_map;
        vector<vector<string>> sublists;

        /* Step 1: Find unique key of every string, store in the hashmap. */
        for (string s : strs) {
            string key = calc_key(s);
            hash_map[key].push_back(s);
        }

        /* Step 2: Grouping of sublists */
        for (auto it : hash_map) {
            sublists.push_back(it.second);
        }

        return sublists;
    }
};
