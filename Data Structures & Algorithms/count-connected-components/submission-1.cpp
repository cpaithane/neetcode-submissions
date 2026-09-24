class Solution {
private:
    unordered_map<int, vector<int>> graph;
    unordered_set<int> visited;

    void dfs(int node) {
        if (visited.find(node) != visited.end()) {
            return;
        }

        visited.insert(node);
        for (int n : graph[node]) {
            dfs(n);
        }
    }

public:
    int countComponents(int n, vector<vector<int>>& edges) {
        int connected = 0;

        for (int i = 0; i < n; i++) {
            graph[i] = {};
        }

        for (auto &edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        for (int i = 0; i < n; i++) {
            if (visited.find(i) == visited.end()) {
                dfs(i);
                connected++;
            }
        }

        return connected;
    }
};
