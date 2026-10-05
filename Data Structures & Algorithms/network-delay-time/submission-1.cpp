class Solution {
private:
    map<int, vector<pair<int, int>>> graph;
    unordered_set<int> visited;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;

public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        int t;

        for (int i = 0; i < (n + 1); i++) {
            graph[i] = {};
        }

        for (auto &time : times) {
            graph[time[0]].push_back({time[1], time[2]});
        }

        heap.push({0, k});
        t = 0;

        while (heap.empty() == false) {
            auto [w, node] = heap.top();
            heap.pop();

            if (visited.find(node) != visited.end()) {
                continue;
            }

            visited.insert(node);
            t = w;

            for (auto [node2, w2] : graph[node]) {
                if (visited.find(node2) == visited.end()) {
                    heap.push({w + w2, node2});
                }
            }
        }

        if (visited.size() == n) {
            return t;
        }
        return -1;
    }
};
