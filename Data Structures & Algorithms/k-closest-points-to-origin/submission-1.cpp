class Solution {
private:
    vector<vector<int>> res;
    priority_queue<pair<double, vector<int>>> heap;

public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        for (auto &point : points) {
            double dist = sqrt(pow(point[0] - 0, 2) + pow(point[1] - 0, 2));

            if (heap.size() < k) {
                heap.push({dist, point});
            } else {
                auto &[top_dist, top_point] = heap.top();

                if (top_dist > dist) {
                    heap.pop();
                    heap.push({dist, point});
                }
            }
        }

        while (!heap.empty()) {
            auto &[dist, point] = heap.top();
            res.push_back(point);
            heap.pop();
        }

        return res;
    }
};
