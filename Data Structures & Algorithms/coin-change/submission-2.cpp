class Solution {
private:
    unordered_map<int, int> dp;

    int coin_change_core(vector<int>& coins, int amount) {
        int res = INT_MAX;

        if (dp.find(amount) != dp.end()) {
            return dp[amount];
        }

        if (amount == 0) {
            dp[amount] = 0;
            return 0;
        }

        for (auto &coin : coins) {
            if ((amount - coin) >= 0) {
                int sub_res = coin_change_core(coins, (amount - coin));
                if (sub_res != INT_MAX) {
                    res = min(res, 1 + sub_res);
                }
            }
        }

        dp[amount] = res;
        return res;
    }

public:
    int coinChange(vector<int>& coins, int amount) {
        int res = coin_change_core(coins, amount);
        if (res == INT_MAX) {
            return -1;
        }

        return res;
    }
};
