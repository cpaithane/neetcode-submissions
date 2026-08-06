class Solution {
public:
    bool dfs(string src, 
             unordered_map<string, vector<string>> adj_list,
             int target_len,
             vector<string> &res) {

            if (res.size() == target_len) {
                return true;
            }
            if (adj_list.find(src) == adj_list.end()) {
                return false;
            }

            vector<string> temp = adj_list[src];
            for (int i = 0; i < temp.size(); i++) {
                string v = temp[i];
                adj_list[src].erase(adj_list[src].begin() + i);
                res.push_back(v);
                if (dfs(v, adj_list, target_len, res) == true) {
                    return true;
                }
                adj_list[src].insert(adj_list[src].begin() + i, v);
                res.pop_back();
            }
        return false;
    }

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, vector<string>> adj_list;
        vector<string> res = {"JFK"};

        for (vector<string> ticket : tickets) {
            adj_list[ticket[0]];
        }

        sort(tickets.begin(), tickets.end());
        /* Build adjacency list. */
        for (vector<string> ticket : tickets) {
            adj_list[ticket[0]].push_back(ticket[1]);
        }

        /* Start DFS from JFK. */
        dfs("JFK", adj_list, tickets.size() + 1, res);
        return res;
    }
};
