class Solution {
private:
    unordered_map<int, vector<int>> graph;
    unordered_set<int> visited;

    bool is_cycle(int node, int parent) {
        if (visited.find(node) != visited.end()) {
            return true;
        }

        visited.insert(node);
        for (int n : graph[node]) {
            if (n == parent) {
                continue;
            }

            if (is_cycle(n, node) == true) {
                return true;
            }
        }

        return false;
    }

public:
    bool validTree(int n, vector<vector<int>>& edges) {
        for (int i = 0; i < n; i++) {
            graph[i] = {};
        }

        for (auto &edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        return (is_cycle(0, -1) == false && visited.size() == n);
    }
};
