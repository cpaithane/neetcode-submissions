class Solution {
public:
    int sum_of_squares(int n) {
        int res = 0;
        int digit = 0;

        while (n != 0) {
            digit = n % 10;
            digit = digit * digit;
            res = res + digit;

            n = n / 10;
        }

        return res;
    }

    bool isHappy(int n) {

        int slow = n;
        int fast = sum_of_squares(n);

        while (slow != fast) {
            slow = sum_of_squares(slow);
            fast = sum_of_squares(fast);
            fast = sum_of_squares(fast);
        }

        if (fast == 1) {
            return true;
        } else {
            return false;
        }

        unordered_set<int> visited;

        while (visited.find(n) == visited.end()) {
            visited.insert(n);

            n = sum_of_squares(n);
            if (n == 1) {
                return true;
            }
        }

        return false;
    }
};
