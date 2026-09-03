class Solution {
public:
    int maxArea(vector<int>& heights) {
        int s, e, max_area;

        s = 0, e = heights.size() - 1, max_area = 0;

        while (s < e) {
            int area = (e - s) * min(heights[e], heights[s]);
            max_area = max(max_area, area);

            if (heights[s] < heights[e]) {
                s++;
            } else if (heights[s] > heights[e]) {
                e--;
            } else {
                s++, e--;
            }
        }

        return max_area;
    }
};
