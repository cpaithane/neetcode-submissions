class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start, max_len;
        unordered_set<char> hash;

        start = 0, max_len = 0;

        for (int end = 0; end < s.size(); end++) {
            while (hash.find(s[end]) != hash.end()) {
                hash.erase(s[start]);
                start++;
            }

            hash.insert(s[end]);
            max_len = max(max_len, (end - start + 1));
        }

        return max_len;
    }
};
