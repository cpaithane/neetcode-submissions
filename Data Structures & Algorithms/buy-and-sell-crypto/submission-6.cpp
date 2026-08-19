class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l, r, max_profit;

        l = 0, r = 1, max_profit = 0;

        while (r < prices.size()) {
            if (prices[l] < prices[r]) {
                max_profit = max(max_profit, (prices[r] - prices[l]));
            } else {
                l = r;
            }

            r++;
        }

        return max_profit;
    }
};
