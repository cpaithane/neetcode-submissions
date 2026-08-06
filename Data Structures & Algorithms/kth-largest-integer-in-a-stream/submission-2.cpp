class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

public:
    KthLargest(int k, vector<int>& nums) {
        /*
         * Insert values in the vector to the priority queue using
         * add method. Ignore the return value of the add().
         */
        for (int x : nums) {
            this->minHeap.push(x);
        }
        this->k = k;
    }
    
    int add(int val) {
        this->minHeap.push(val);

        /*
         * Pop from maxHeap only if its size is greater than k.
         * Return top of the heap after popping.
         */
        while (this->minHeap.size() > this->k) {
            this->minHeap.pop();
        }
        return this->minHeap.top();
    }
};
