class Solution {
private:
    priority_queue<int, vector<int>, greater<int>> min_heap;

public:
    int findKthLargest(vector<int>& nums, int k) {
        
        for (int num : nums) {
            if (min_heap.size() < k) {
                min_heap.push(num);
            } else {
                int top = min_heap.top();

                if (top < num) {
                    min_heap.pop();
                    min_heap.push(num);
                }
            }
        }

        if (min_heap.size() > 0) {
            return min_heap.top();
        }

        return 0;
    }
};
