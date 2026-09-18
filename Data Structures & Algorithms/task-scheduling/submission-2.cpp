class Solution {
private:
    unordered_map<char, int> freq;
    priority_queue<int> heap;
    queue<pair<int, int>> q;
    int cycles;

public:
    int leastInterval(vector<char>& tasks, int n) {
        for (char &ch : tasks) {
            freq[ch] += 1;
        }

        for (auto &[ch, f] : freq) {
            heap.push(f);
        }

        cycles = 0;
        while (heap.size() > 0 || q.size()) {
            cycles++;

            if (heap.size() > 0) {
                int f = heap.top() - 1;
                heap.pop();

                if (f > 0) {
                    q.push({f, cycles + n});
                }
            } else {
                cycles = q.front().second;
            }

            if (q.size() > 0 && q.front().second == cycles) {
                heap.push(q.front().first);
                q.pop();
            }
        }

        return cycles;
    }
};
