class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> kv;

public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        kv[key].emplace_back(timestamp, value);        
    }
    
    string get(string key, int timestamp) {
        auto &val_list = kv[key];
        int l = 0;
        int r = val_list.size() - 1;
        string res = "";

        while (l <= r) {
            int m = (l + (r - l) / 2);

            if (val_list[m].first <= timestamp) {
                res = val_list[m].second;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return res;
    }
};
