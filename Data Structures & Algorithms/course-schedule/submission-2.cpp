class Solution {
private:
    unordered_set<int> visited;
    unordered_map<int, vector<int>> graph;

    bool dfs(int node, unordered_map<int, vector<int>> &graph) {
        if (visited.find(node) != visited.end()) {
            return true;
        }

        visited.insert(node);
        for (int n : graph[node]) {
            if (dfs(n, graph)) {
                return true;
            }
        }

        visited.erase(node);
        graph[node].clear();
        return false;
    }

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int count = 0;

        for (int i = 0; i < numCourses; i++) {
            graph[i] = {};
        }

        for (auto &pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
        }

        for (auto &[node, neighbors] : graph) {
            if (dfs(node, graph)) {
                return false;
            }

            count++;
        }

        if (count == numCourses) {
            return true;
        }
        return false;
    }
};
