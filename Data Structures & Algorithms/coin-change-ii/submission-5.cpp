class Solution {
private:
    map<pair<int, int>, int> dp;

    int change_core(int i, int amount, vector<int>& coins) {
        int ways;

        if (i >= coins.size()) {
            return 0;
        }

        if (amount == 0) {
            return 1;
        }

        if (dp.find({i, amount}) != dp.end()) {
            return dp[{i, amount}];
        }

        ways = 0;
        if (amount >= coins[i]) {
            ways = change_core(i, amount - coins[i], coins);
            ways += change_core(i + 1, amount, coins);
        }

        dp[{i, amount}] = ways;
        return ways;
    }

public:
    int change(int amount, vector<int>& coins) {
        sort(coins.begin(), coins.end());
        return change_core(0, amount, coins);
    }
};
