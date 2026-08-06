#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> hash;
        for (int x : nums) {
            if (hash.find(x) == hash.end()) {
                hash.insert(x);
            } else {
                return true;
            }
        }
        return false;
    }
};
