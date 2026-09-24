class Solution {
private:
    unordered_map<int, vector<int>> graph;
    unordered_set<int> visited;
    unordered_set<int> cycle;
    int cycle_start;

    bool dfs(int node, int parent) {
        if (visited.find(node) != visited.end()) {
            cycle_start = node;
            return true;
        }

        visited.insert(node);
        for (int n : graph[node]) {
            if (n == parent) {
                continue;
            }

            if (dfs(n, node) == true) {
                if (cycle_start != -1) {
                    cycle.insert(n);
                }
                
                if (node == cycle_start) {
                    cycle_start = -1;
                }

                return true;
            }
        }
        return false;
    }

public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        cycle_start = -1;
        vector<int> res_list;

        for (int i = 0; i < edges.size(); i++) {
            graph[i] = {};
        }

        for (auto &edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        dfs(1, -1);

        for (int i = edges.size() - 1; i >= 0; i--) {
            auto &edge = edges[i];

            if (cycle.find(edge[0]) != cycle.end() &&
                cycle.find(edge[1]) != cycle.end()) {
                res_list.push_back(edge[0]);
                res_list.push_back(edge[1]);
                return res_list;
            }
        }

        return res_list;
    }
};
