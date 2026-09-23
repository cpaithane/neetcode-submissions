class Solution {
private:
    unordered_map<int, vector<int>> graph;
    queue<int> q;
    vector<int> res_list;

public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegrees(numCourses);
        for (int c = 0; c < numCourses; c++) {
            graph[c] = {};
        }

        for (auto &pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
            indegrees[pre[0]]++;
        }

        for (int i = 0; i < numCourses; i++) {
            if (indegrees[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int n = q.front();
            q.pop();
            res_list.push_back(n);

            for (int node : graph[n]) {
                indegrees[node]--;

                if (indegrees[node] == 0) {
                    q.push(node);
                }
            }
        }

        if (res_list.size() == numCourses) {
            return res_list;
        }
        return {};
    }
};
