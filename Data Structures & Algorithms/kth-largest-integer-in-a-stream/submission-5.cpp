class KthLargest {
    /*
     * kth largest element in the heap is the smallest element in the heap of size K.
     * That's why, use min_heap, not max_heap.
     */
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> min_heap;

public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;

        for (int &num : nums) {
            this->min_heap.push(num);
        }
    }
    
    int add(int val) {
        this->min_heap.push(val);

        while (this->min_heap.size() > this->k) {
            this->min_heap.pop();
        }

        return this->min_heap.top();
    }
};
