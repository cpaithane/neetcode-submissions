class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l, r, res;

        l = 1;
        r = 0;

        // search space is 1 to max of piles.
        for (int &p : piles) {
            r = max(r, p);
        }
        res = r;

        while (l <= r) {

            // reduce the search space.
            int k = (l + (r - l)/2);
            long long total = 0;

            for (int &p : piles) {
                total += ceil((double) p / k);
            }

            if (total <= h) {
                res = k;
                r = k - 1;
            } else {
                l = k + 1;
            }

        }
        return res;
    }
};
