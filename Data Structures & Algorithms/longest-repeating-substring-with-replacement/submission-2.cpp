class Solution {
public:
    int characterReplacement(string s, int k) {
        int l, r, res, max_freq;
        unordered_map<char, int> hash;
        l = 0, res = 0, max_freq = 0;

        for (r = 0; r < s.size(); r++) {
            int freq = 1 + hash[s[r]];
            hash[s[r]] = freq;
            max_freq = max(freq, max_freq);

            while (((r - l + 1) - max_freq) > k) {
                hash[s[l]] -= 1;
                l++;
            }

            res = max(res, (r - l + 1));
        }

        return res;
    }
};
