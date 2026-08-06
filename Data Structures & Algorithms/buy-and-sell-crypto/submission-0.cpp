class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /* Profit must be maximized. Initialize with 0. */
        int max_profit = 0;

        /* Minimum value in the left part of the array. */
        int min_left = prices[0];

        for (int price:prices) {
            if (min_left > price) {
                min_left = price;
            }

            int profit = price - min_left;
            if (profit > max_profit) {
                max_profit = profit;
            }
        }
        return max_profit;
    }
};
