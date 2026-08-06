class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /* Profit must be maximized. Initialize with 0. */
        int max_profit = 0;

        /* Minimum value in the left part of the array. */
        int min_left = prices[0];

        for (int price:prices) {
            /* Min left so far is less than the price, update min left */
            if (min_left > price) {
                min_left = price;
            }

            /* If profit so far is max than previous profits, update max_profit. */
            int profit = price - min_left;
            if (profit > max_profit) {
                max_profit = profit;
            }
        }
        return max_profit;
    }
};
