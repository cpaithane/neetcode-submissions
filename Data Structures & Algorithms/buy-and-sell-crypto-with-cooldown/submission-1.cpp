class Solution {
    map<pair<int, bool>, int> dp;

private:
    int max_profit_core(int i, bool buying, vector<int>& prices) {
        int buy_profit, cool_profit, sell_profit, profit;

        if (i >= prices.size()) {
            return 0;
        }

        if (dp.find({i, buying}) != dp.end()) {
            return dp[{i, buying}];
        }

        if (buying == true) {
            buy_profit = max_profit_core(i + 1, !buying, prices) - prices[i];
            cool_profit = max_profit_core(i + 1, buying, prices);
            profit = max(buy_profit, cool_profit);
        } else {
            sell_profit = max_profit_core(i + 2, !buying, prices) + prices[i];
            cool_profit = max_profit_core(i + 1, buying, prices);
            profit = max(sell_profit, cool_profit);
        }

        dp[{i, buying}] = profit;
        return profit;
    }

public:
    int maxProfit(vector<int>& prices) {
        return max_profit_core(0, true, prices);
    }
};
