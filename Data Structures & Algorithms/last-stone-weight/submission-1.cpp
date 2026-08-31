class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> max_heap;

        for (int &s : stones) {
            max_heap.push(s);
        }

        while (max_heap.size() > 1) {
            int heavy1 = max_heap.top();
            max_heap.pop();

            int heavy2 = max_heap.top();
            max_heap.pop();

            if (heavy2 < heavy1) {
                max_heap.push(heavy1 - heavy2);
            }
        }

        if (max_heap.size() == 0) {
            return 0;
        }
        return max_heap.top();
    }
};
