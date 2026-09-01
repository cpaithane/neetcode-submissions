class Solution {
public:
    int hammingWeight(uint32_t n) {
        int nr_set = 0;

        while (n != 0) {
            n = n & (n - 1);
            nr_set++;
        }

        return nr_set;
    }
};
